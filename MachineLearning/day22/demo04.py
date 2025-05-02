# 三维数组可以从三个方向来进行连接
import numpy as np

a = np.arange(1, 9).reshape(2, 2, 2)
b = np.arange(9, 17).reshape(2, 2, 2)
print(a)
print(b)
c = np.concatenate((a, b), axis=2)
print(c)

# axis = 0:深度方向上连接 对应z
# axis = 1:纵向 对应y
# axis = 2:横向 对应x
