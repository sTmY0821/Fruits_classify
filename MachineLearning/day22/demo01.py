"""
数组维度操作：对维度进行变换
1.共享变维  改变后的数据与之前的数据共享地址 reshape
2.复制变维  改变后的数据不影响之前的数据 revel
"""
import numpy as np
a = np.arange(1,9,1)

print(a.reshape(2,4))

print(a.reshape(2,2,2))
#ravel：扁平化，将数组拍扁为1维（使用原数据）
#flatten不同于ravel，flatten会复制数据
print(a.reshape(2,2,2).ravel())

#mask 数据掩码
mask = a >2
print(mask)
print(a[mask])