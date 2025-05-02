import numpy as np
import matplotlib.pyplot as mp
import math

x = np.arange(-5, 5, 0.1)
y = x ** 2
mp.plot(x,y,label='$y=x^2$',linewidth = 2,color = 'red',alpha = 0.5)
mp.xlabel('x')
mp.ylabel('y')
mp.xlim(-10,10)
mp.ylim(-1,30)
x_tck = np.arange(-10,10,2)
x_txt = x_tck.astype("U")
mp.xticks(x_tck,x_txt)
y_tck = np.arange(-1,30,5)
y_txt = y_tck.astype("U")
mp.yticks(y_tck)

mp.title("square")
mp.legend(loc = 'upper right')
mp.show()