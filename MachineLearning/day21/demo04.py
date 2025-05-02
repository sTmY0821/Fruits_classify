import numpy as np
#complex复数数组
arr = np.array([[1+2j, 3+4j, 5+6j],
               [4+8j,5+10j,6+12j]]
               )
print(arr)
for x in arr.flat:#扁平迭代，转换为一维数组然后迭代
    print(x.real,",",x.imag)