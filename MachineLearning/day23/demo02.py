
import numpy as np
import matplotlib.pyplot as mp
import math

x = np.arange(0,2 * np.pi, 0.1)
print(x)
print(x.shape)

y1 = np.sin(x)
y2 = np.cos(x)

mp.plot(x, y1, label='sin', linewidth=2)
mp.plot(x,y2,label= 'cos',linestyle = '--',linewidth=2)
mp.show()
