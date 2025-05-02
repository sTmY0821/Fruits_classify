import numpy as np
import math
import matplotlib.pyplot as mp

x = np.array([
    [0.1],
    [0.2],
    [0.3], [0.4], [0.5], [0.6], [0.7], [0.8], [0.9]])
y = []
for i in range(len(x)):
    y_value = 1-x[i]
    y.append(-x[i]*math.log(x[i])-y_value*math.log(y_value))

mp.figure("entropy change", facecolor="lightgray")
mp.title("entropy change", fontsize=20)
mp.xlabel("x", fontsize=14)
mp.ylabel("y", fontsize=14)
mp.grid(linestyle=":")
mp.tick_params(labelsize=10)
mp.plot(x, y, c="red", label="entropy change")
mp.legend()
mp.show()
