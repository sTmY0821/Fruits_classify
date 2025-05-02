# 线性回归示例
import numpy as np
# 线性模型
import sklearn.linear_model as lm
# 模型性能评价模块
import sklearn.metrics as sm
import matplotlib.pyplot as mp
x,y=[],[]
with open("../data/single.txt", "r")as f:
    for line in f.readlines():
        data_x, data_y = line.strip().split(",")
        x.append([float(data_x)])
        y.append(float(data_y))

x = np.array(x)
y = np.array(y)
model = lm.LinearRegression()
model.fit(x, y)
y_predict = model.predict(x)
print("斜率：", model.coef_)
print("截距：", model.intercept_)
print("模型性能：", sm.r2_score(y, model.predict(x)))

mp.figure("Linear Regression", facecolor="lightgray")
mp.title("Linear Regression", fontsize=16)
mp.xlabel("x", fontsize=14)
mp.ylabel("y", fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=":")
mp.plot(x, y_predict, c="dodgerblue", alpha=0.8, label="Sample")
mp.scatter(x, y, c="orangered", alpha=0.8, s=60, label="Pre")
mp.legend()
mp.show()



