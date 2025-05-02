import numpy as np
import matplotlib.pyplot as mp
import math

ax = mp.gca()
axis_b = ax.spines['bottom']
axis_b.set_position(('data', 0))

var = lambda y, b: y * b