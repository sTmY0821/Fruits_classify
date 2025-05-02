import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 2, 3, 4])
print(a)
print(b)
print("=======================")
# 填充b数组使其长度与a相同
b = np.pad(b, pad_width=(1, 1),  # 对b进行填充，左边填充0个，右边填充1个
           mode='constant',  # 填充常数值
           constant_values=-1)  # 填充常数值为-1
print(b)
print("=======================")
# 垂直方向完成组合操作，生成新数组
# c = np.vstack((a, b))
# print(c)
