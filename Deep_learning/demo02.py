'''
基于python代码实现全连接的正向传播
'''
import numpy as np
#第一层
x = np.array([[5.0,10.0]])
w = np.random.normal(0.1,size = (2,3))
b = np.ones(shape=3,)
prey_y1 = x*w+b
#第二层
w2 = np.mat(np.random.normal(0,1,size=(3,1)))
b2 = np.mat(np.ones(2,))
prey_y2 = prey_y1*w2+b2

#第三层
w3 = np.mat(np.random.normal(0,1,size=(2,2)))
b3 = np.mat(np.ones(2,))
prey_y3 = prey_y2*w3+b3