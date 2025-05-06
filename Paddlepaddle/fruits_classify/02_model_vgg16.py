"""
搭建模型，训练模型，保存模型
"""
import paddle
import paddle.fluid as fluid
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

from temp import *
from multiprocessing import cpu_count
import os
import numpy as np


# 构建数据读取器

def train_mapper(sample):
    img_path, label = sample
    if os.path.exists(img_path):
        # 读取图像数据
        img = paddle.dataset.image.load_image(img_path, is_color=True)
        # 对图像进行缩放，固定到相同尺寸
        img = paddle.dataset.image.simple_transform(img,
                                                    resize_size=image_size,
                                                    crop_size=image_size,
                                                    is_color=True,
                                                    is_train=True)
        # 对图像进行归一化
        img = img.astype('float32') / 255.0
        return img, int(label)  # img变为了c(通道数）,w,h


def train_r(train_file):
    def reader():
        with open(train_file, 'r') as f:
            for line in f:
                img_path,label = line.strip().split('\t')
                yield img_path, int(label)

    return paddle.reader.xmap_readers(reader=reader,
                                      mapper=train_mapper,
                                      process_num=cpu_count(),
                                      buffer_size=1173)


def test_mapper(sample):
    img_path, label = sample
    if os.path.exists(img_path):
        # 读取图像数据
        img = paddle.dataset.image.load_image(img_path, is_color=True)
        # 对图像进行缩放，固定到相同尺寸
        img = paddle.dataset.image.simple_transform(img,
                                                    resize_size=image_size,
                                                    crop_size=image_size,
                                                    is_color=True,
                                                    is_train=False)
        # 对图像进行归一化
        img = img.astype('float32') / 255.0
        return img, int(label)  # img变为了c(通道数）,w,h


def test_r(test_file):
    def reader():
        with open(test_file, 'r') as f:
            for line in f:
                img_path,label = line.strip().split('\t')
                yield img_path, int(label)

    return paddle.reader.xmap_readers(reader=reader,
                                      mapper=test_mapper,
                                      process_num=cpu_count(),
                                      buffer_size=133)


# 训练集读取器
train_reader = train_r(train_file_path)
train_shuffle_reader = paddle.reader.shuffle(train_reader, buf_size=1173)
train_batch_reader = paddle.batch(train_shuffle_reader, batch_size=batch_size)
# 测试集读取器
test_reader = test_r(test_file_path)
test_shuffle_reader = paddle.reader.shuffle(test_reader, buf_size=133)
test_batch_reader = paddle.batch(test_shuffle_reader, batch_size=batch_size)

# 模型搭建
# 占位符:
x = fluid.layers.data(name='x', shape=[3, image_size, image_size], dtype='float32')
y = fluid.layers.data(name='y', shape=[1], dtype='int64')


def vggnet16_convolution_neural_network(image):
    """
    创建CNN
    :param image: 图像数据
    :param type_size: 输出类别数量
    :return: 分类概率
    模型结构：
    """

    def conv_block(input,num_filter,groups):
        conv_pool = fluid.nets.img_conv_group(
            input=input,
            conv_num_filter=[num_filter] * groups,
            pool_size=vgg_params['pool_size'],
            conv_padding=vgg_params['conv_padding'],
            conv_filter_size=vgg_params['conv_filter_size'],
            conv_act=vgg_params['conv_act'],
            pool_stride=vgg_params['pool_stride'],
            pool_type = vgg_params['pool_type'],
            )
        return conv_pool
    conv1 = conv_block(image,64,2)
    conv2 = conv_block(conv1,128,2)
    conv3 = conv_block(conv2,256,3)
    conv4 = conv_block(conv3,512,3)
    conv5 = conv_block(conv4,512,3)
    drop = fluid.layers.dropout(x=conv5, dropout_prob=dropout_prob)
    fc1 = fluid.layers.fc(input=drop, size=512, act='relu')
    bn = fluid.layers.batch_norm(input=fc1,act='relu')
    drop2 = fluid.layers.dropout(x=bn, dropout_prob=dropout_prob)
    fc2 = fluid.layers.fc(input=drop2, size=512, act='relu')
    predict = fluid.layers.fc(input=fc2, size=5, act='softmax')
    return predict


pred_y = vggnet16_convolution_neural_network(image=x)

# 损失函数
cost = fluid.layers.cross_entropy(input=pred_y, label=y)  # 交叉熵
avg_cost = fluid.layers.mean(cost)
# 精度
accuracy = fluid.layers.accuracy(input=pred_y, label=y)
#克隆一个program用于测试
test_program = fluid.default_main_program().clone(for_test=True)
# 梯度下降(优化器）
optimizer = fluid.optimizer.Adam(learning_rate=learning_rate)
optimizer.minimize(avg_cost)

# 执行器
place = fluid.CPUPlace()
exe = fluid.Executor(place)
# 初始化
exe.run(fluid.default_startup_program())

#检查路径是否存在模型
if os.path.exists(vgg_train_path):
    fluid.io.load_persistables(exe, vgg_train_path, fluid.default_main_program())
    print("增量加载成功")
# 训练模型
feeder = fluid.DataFeeder(feed_list=[x, y], place=place)
for pass_id in range(epoch_num):
    train_costs, train_accs = [], []
    for train_data in train_batch_reader():
        train_cost, train_acc = exe.run(program=fluid.default_main_program(),
                                        feed=feeder.feed(train_data),
                                        fetch_list=[avg_cost, accuracy])
        train_costs.append(train_cost[0])
        train_accs.append(train_acc[0])
    avg_train_cost = np.mean(train_costs)
    avg_train_acc = np.mean(train_accs)
    print(f'轮数:{pass_id + 1},cost:{avg_train_cost},accuracy:{avg_train_acc}')
    iters.append(pass_id + 1)
    costs.append(avg_train_cost)

# 测试模型
test_data = next(test_batch_reader())

test_acc =exe.run(program=test_program,
        feed = feeder.feed(test_data),
        fetch_list=[accuracy])
print(f'测试集准确率:{test_acc[0][0]}')

#保存增量模型
fluid.io.save_persistables(executor=exe, dirname=vgg_train_path,main_program=fluid.default_main_program())
print('增量模型保存成功')
#保存推理模型
fluid.io.save_inference_model(dirname=vgg_infer_path,
                              feeded_var_names=['x'],
                              target_vars=[pred_y],
                              executor=exe)
print('推理模型保存成功')


#训练结果可视化
plt.figure("train_cost", figsize=(12, 7), facecolor='lightgray')
plt.title("Train Cost", fontsize=48)
plt.xlabel("epoch", fontsize=14)
plt.ylabel("cost", fontsize=14)
plt.plot(iters, costs, color="red", label="train cost", linewidth=1.0)
plt.savefig("train_cost.png")