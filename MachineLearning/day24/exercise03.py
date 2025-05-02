# 数据预处理之：归一化
import numpy as np
import sklearn.preprocessing as sp

# 样本数据
raw_samples = np.array([
    [10.0, 20.0, 5.0],
    [8.0, 10.0, 1.0]
])
# print(raw_samples)
# nor_samples = raw_samples.copy()  # 复制样本数据
#
# for row in nor_samples:
#     row /= abs(row).sum()  # 先对行求绝对值，再求和，再除以绝对值之和
#
# print(nor_samples) # 打印结果

nor = sp.normalize(raw_samples, norm='l2')
nor1 = sp.normalize(raw_samples, norm='l1')
print(nor)
print(nor1)