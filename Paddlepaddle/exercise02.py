# 波士顿放假预测
import os.path

import paddle.fluid as fluid
import numpy as np
import matplotlib.pyplot as plt
import paddle

# 数据准备
random_reader = paddle.reader.shuffle(paddle.dataset.uci_housing.train(), buf_size=404)
train_reader = paddle.batch(random_reader, batch_size=64)

# 搭建网络
x = fluid.layers.data("x", shape=[13], dtype='float32')
y = fluid.layers.data("y", shape=[1], dtype='float32')
# 第一层
fc1 = fluid.layers.fc(input=x, size=512, act="sigmoid")
# 第二层
fc2 = fluid.layers.fc(input=fc1, size=512, act="sigmoid")
# 输出层
y_predict = fluid.layers.fc(input=fc2, size=1)
cost = fluid.layers.square_error_cost(input=y_predict,
                                      label=y)
avg_cost = fluid.layers.mean(cost)
# # 优化器
# optimizer = fluid.optimizer.SGDOptimizer(learning_rate=0.01)
# opts = optimizer.minimize(avg_cost)
# 学习率衰减优化器
optimizer_adam = fluid.optimizer.Adam(learning_rate=0.001)
opts = optimizer_adam.minimize(avg_cost)

# 模型训练、评估
place = fluid.CPUPlace()
feeder = fluid.DataFeeder(feed_list=[x, y], place=place)
exe = fluid.Executor(place)
exe.run(fluid.default_startup_program())
iters = []
costs = []

# 在开始训练之前检查是否有模型保存了
if os.path.exists('model/boston/train/'):
    fluid.io.load_persistables(executor=exe, dirname='model/boston/train/',
                               main_program=fluid.default_main_program())
    print('模型加载成功')
else:
    for pass_id in range(200):  # 迭代次数
        train_cost_list = []
        for data in train_reader():
            train_cost = exe.run(program=fluid.default_main_program(), feed=feeder.feed(data), fetch_list=[avg_cost])
            train_cost_list.append(train_cost[0][0])
        train_cost_avg = np.array(train_cost_list).mean()
        print("第{}次迭代，平均损失为{}".format(pass_id, train_cost_avg))
        # 准备可视化数据
        iters.append(pass_id + 1)
        costs.append(train_cost_avg)


# 保存增量模型
model_train_path = 'model/boston/train/'
fluid.io.save_persistables(executor=exe, dirname=model_train_path, main_program=fluid.default_main_program())
print(f'增量模型保存成功:{model_train_path}')

#保存推理模型
model_infer_path = 'model/boston/infer/'
fluid.io.save_inference_model(model_infer_path, ['x'], [y_predict], exe)
print(f'推理模型保存成功:{model_infer_path}')
# 可视化
plt.figure("train_cost", figsize=(12, 7), facecolor='lightgray')
plt.title("Train Cost", fontsize=48)
plt.xlabel("epoch", fontsize=14)
plt.ylabel("cost", fontsize=14)
plt.plot(iters, costs, color="red", label="train cost", linewidth=1.0)
plt.grid()
plt.show()
plt.savefig("train_cost.png")
