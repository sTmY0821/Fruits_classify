import numpy as np
#创建数组：np.array or np.arange
#数组：要求元素数据类型一致
arr = np.array([1, 2, 3, 4, 5]) #一维数组 [1,2,3,4,5]为列表
print(type(arr))
print(arr)

#arange:创建数组是在指定的范围内以指定的间隔创建
arr2 = np.arange(0,5,1) #从0到5（不含5），步长为1
print(arr2)

#创建全为0 的数组：np.zeros(shape)
arr3 = np.zeros(10)
print(arr3)

#创建全为1 的数组：np.ones(shape)
arr4 = np.ones(10)
print(arr4)

