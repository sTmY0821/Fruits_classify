"""
搭建模型，训练模型，保存模型
"""
import paddle
import paddle.fluid as fluid
from temp import *
from multiprocessing import cpu_count
import os
import numpy as np


# 构建数据读取器

def train_mapper(sample):
    label, img_path = sample
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
        return int(label), img  # img变为了c(通道数）,w,h


def train_r(train_file):
    def reader():
        with open(train_file, 'r') as f:
            for line in f:
                label, img_path = line.strip().split('\t')
                yield label, img_path

    return paddle.reader.xmap_readers(reader=reader,
                                      mapper=train_mapper,
                                      process_num=cpu_count(),
                                      buffer_size=1173)


def test_mapper(sample):
    label, img_path = sample
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
        return int(label), img  # img变为了c(通道数）,w,h


def test_r(test_file):
    def reader():
        with open(test_file, 'r') as f:
            for line in f:
                label, img_path = line.strip().split('\t')
                yield label, img_path

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


def convolution_neural_network(image):
    """
    创建CNN
    :param image: 图像数据
    :param type_size: 输出类别数量
    :return: 分类概率
    模型结构：
    """

    # 第一组
    conv_pool_1 = fluid.nets.simple_img_conv_pool(
        input=image,
        filter_size=filter_size,  # 卷积核大小
        num_filters=num_filters1,  # 卷积核数量
        pool_size=pool_size,  # 池化核大小
        pool_stride=pool_stride,  # 池化步长
        pool_type=pool_type,  # 池化类型
        pool_padding=pool_padding,  # 池化padding
        conv_stride=conv_stride,  # 卷积步长
        conv_padding=conv_padding,  # 卷积核padding
        act=act)  # 激活函数
    drop1 = fluid.layers.dropout(x=conv_pool_1, dropout_prob=dropout_prob)
    # 第二组
    conv_pool_2 = fluid.nets.simple_img_conv_pool(
        input=drop1,
        filter_size=filter_size,  # 卷积核大小
        num_filters=num_filters2,  # 卷积核数量
        pool_size=pool_size,  # 池化核大小
        pool_stride=pool_stride,  # 池化步长
        pool_type=pool_type,  # 池化类型
        pool_padding=pool_padding,  # 池化padding
        conv_stride=conv_stride,  # 卷积步长
        conv_padding=conv_padding,  # 卷积核padding
        act=act
    )
    drop2 = fluid.layers.dropout(x=conv_pool_2, dropout_prob=dropout_prob)
    # 第三组
    conv_pool_3 = fluid.nets.simple_img_conv_pool(
        input=drop2,
        filter_size=filter_size,  # 卷积核大小
        num_filters=num_filters3,  # 卷积核数量
        pool_size=pool_size,  # 池化核大小
        pool_stride=pool_stride,  # 池化步长
        pool_type=pool_type,  # 池化类型
        pool_padding=pool_padding,  # 池化padding
        conv_stride=conv_stride,  # 卷积步长
        conv_padding=conv_padding,  # 卷积核padding
        act=act
    )
    drop3 = fluid.layers.dropout(x=conv_pool_3, dropout_prob=dropout_prob)

    # 全连接层
    fc = fluid.layers.fc(input=drop3, size=f1_size, act=fc_act)
    drop4 = fluid.layers.dropout(x=fc, dropout_prob=dropout_prob)

    # 输出层
    pred_y = fluid.layers.fc(input=drop4, size=5, act='softmax')

    return pred_y


pred_y = convolution_neural_network(image=x)

# 损失函数
cost = fluid.layers.cross_entropy(input=pred_y, label=y) #交叉熵
avg_cost = fluid.layers.mean(cost)
# 精度
accuracy = fluid.layers.accuracy(input=pred_y, label=y)
#梯度下降(优化器）
optimizer = fluid.optimizer.Adam(learning_rate=learning_rate)
optimizer.minimize(avg_cost)

#执行器
place = fluid.CPUPlace()
exe = fluid.Executor(place)
#初始化
exe.run(fluid.default_startup_program())
#训练模型
feeder = fluid.DataFeeder(feed_list=[x, y], place=place)
for pass_id in range(epoch_num):
    train_costs,train_accs = [],[]
    for train_data in train_batch_reader():
        train_cost,train_acc = exe.run(program=fluid.default_main_program(),
                              feed=feeder.feed(train_data),
                              fetch_list=[avg_cost, accuracy])
        train_costs.append(train_cost[0])
        train_accs.append(train_acc[0])
        avg_train_cost = np.mean(train_costs)
        avg_train_acc = np.mean(train_accs)
        print(f'轮数:{pass_id + 1},cost:{avg_train_cost},accuracy:{avg_train_acc}')
        iters.append(pass_id + 1)
        costs.append(avg_train_cost)

