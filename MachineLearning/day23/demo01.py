import numpy as np
import matplotlib.pyplot as mp

# 绘制简单直线
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 6, 9, 12, 15])
# 绘制水平线、垂线
mp.axhline(y=6, ls="-", c="blue")  # 添加水平直线
mp.axvline(x=4, ls="-", c="red")  # 添加垂直直线
# 绘制多段垂线
mp.vlines([2, 3, 3.5],  # 垂线的x坐标值
          [10, 20, 30],  # 每条垂线起始y坐标
          [25, 35, 45])  # 每条垂线结束y坐标
mp.plot(x, y)
mp.show()  # 显示图片，阻塞方法


