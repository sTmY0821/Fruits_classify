# 数组垂直堆叠（vstack）和 垂直分割（vsplit）
import numpy as np

a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)
print(a)
print(b)
print('-----------------')

c = np.vstack((a, b))
print(c)
d,e = np.vsplit(c,2)#将数组c垂直拆分为两个形状相同的数组
print(d)
print(e)


f = np.hstack((a, b))
print(f)

g,h = np.hsplit(f,2)
print(g)
print(h)