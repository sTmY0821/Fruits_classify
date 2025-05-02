# 定义三维数组，并遍历和打印
import numpy as np

a = np.array([
    [[1, 2, 3, ],
     [3, 4, 5]],  # 第一个二维数组
    [[5, 6, 7],
     [7, 8, 9]]  # 第二个二维数组
])

print(a.shape)# 打印数组的维度
print(a.size)# 打印数组的大小
print(a.dtype)#打印数组元素的类型 (int32:32个bit表示的整数)

#遍历：逐个元素去访问数组
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        for k in range(a.shape[2]):
            print(a[i][j][k])

