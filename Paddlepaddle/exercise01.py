"""
线性回归
"""
import paddle.fluid as fluid
import numpy as np
import matplotlib.pyplot as plt


#数据准备
train_data = np.array([[0.5], [0.6], [0.8], [1.1], [1.4]]).astype('float32')
y_true = np.array([[5.0], [5.5], [6.0], [6.8], [6.8]]).astype('float32')
x = fluid.layers.data(name='x', shape=[1], dtype='float32')
y = fluid.layers.data(name='x', shape=[1], dtype='float32')
y_preict = fluid.layers.fc(input=x, size=1)
cost = fluid.layers.square_error_cost(input=y_preict, label=y)
avg_cost = fluid.layers.mean(cost)

#优化
optimizer = fluid.optimizer.SGD(learning_rate=0.01)
optimizer.minimize(avg_cost)

#搭建网络
place= fluid.CPUPlace()
exe = fluid.Executor(place)
exe.run(fluid.default_startup_program())  # 初始化系统参数

# 开始训练, 迭代100次
costs = []
iters = []
values = []
params = {"x": train_data, "y": y_true}
for i in range(100):
    outs = exe.run(fluid.default_main_program(),
                  feed=params,
                  fetch_list=[avg_cost, y_preict])
    costs.append(outs[0][0])
    iters.append(i+1)
    values.append(outs[1])
    print("第%d次迭代,误差：%s" % (iters[i], costs[i]))

#数据可视化
plt.figure("train_cost",figsize=(12,7),facecolor='lightgray')
plt.xlabel("epoch", fontsize=14)
plt.ylabel("cost", fontsize=14)
plt.title("Train Cost", fontsize=48)
plt.plot(iters,costs,color='red',label='cost')
plt.show()


#模型预测
infer_exe = fluid.Executor(place)
infer_scope = fluid.core.Scope()


