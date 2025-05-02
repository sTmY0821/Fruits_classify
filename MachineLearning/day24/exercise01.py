# 数据预处理之：均值移除示例
import numpy as np
import sklearn.preprocessing as sp #数据预处理模块

# 样本数据
raw_samples = np.array([
    [3.0, -1.0, 2.0],
    [0.0, 4.0, 3.0],
    [1.0, -4.0, 2.0]
])
# print(raw_samples)
# print(raw_samples.mean(axis=0))  # 求每列的平均值
# print(raw_samples.std(axis=0))  # 求每列标准差
#
# std_samples = raw_samples.copy()  # 复制样本数据
# for col in std_samples.T:  # 遍历每列
#     col_mean = col.mean()  # 计算平均数
#     col_std = col.std()  # 求标准差
#     col -= col_mean  # 减平均值
#     col /= col_std  # 除标准差
#
# print(std_samples)
# print(std_samples.mean(axis=0))
# print(std_samples.std(axis=0))

std_samples =sp.scale(raw_samples)
print(std_samples)
print(std_samples.mean(axis=0))
print(std_samples.std(axis=0))
