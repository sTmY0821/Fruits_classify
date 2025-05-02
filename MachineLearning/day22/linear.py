import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(0,10,50)
y = 0.8*x**2+4*x-5
mp.plot(x,y,color = "red")
mp.show()