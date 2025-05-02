# 使用随机森林实现共享单车使用量预测

import csv
import numpy as np
import sklearn.utils as su
import sklearn.ensemble as se
import sklearn.metrics as sm
import matplotlib.pyplot as mp

x, y = [], []
with open("../data/bike_day.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        x.append(row[2:13])  # 第1列序号掐掉, 挑出其中的输入
        y.append(row[-1])  # 最后一列是输出

fn_dy = np.array(x[0]) # 保存特征名称
x = np.array(x[1:], dtype=float) # 去掉第1行标题部分
y = np.array(y[1:], dtype=float) # 去掉第1行标题部分

# 将矩阵打乱
x = su.shuffle(x, random_state=7)
y = su.shuffle(y, random_state=7)

# 计算训练数据的笔数，创建训练集、测试集
train_size = int(len(x) * 0.9)  # 用90%的数据来训练模型

train_x = x[:train_size]  # 训练输入
train_y = y[:train_size]  # 训练输出

test_x = x[train_size:]  # 测试输入
test_y = y[train_size:]  # 测试输出

# 创建随机森林回归器，并进行训练
model = se.RandomForestRegressor(max_depth=10, #最大深度
                                 n_estimators=1000, #树数量
                                 min_samples_split=2) #最小样本数量，小于该数就不再划分子节点
model.fit(train_x, train_y)  # 训练

# 基于天统计数据的特征重要性
fi_dy = model.feature_importances_
# print(fi_dy)
pre_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pre_test_y)) #打印r2得分

# 可视化
mp.figure('Bike', facecolor='lightgray')
mp.subplot(211)
mp.title('Day', fontsize=16)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
sorted_idx = fi_dy.argsort()[::-1]
pos = np.arange(sorted_idx.size)
mp.bar(pos, fi_dy[sorted_idx], facecolor='deepskyblue', edgecolor='steelblue')
mp.xticks(pos, fn_dy[sorted_idx], rotation=30)

mp.show()