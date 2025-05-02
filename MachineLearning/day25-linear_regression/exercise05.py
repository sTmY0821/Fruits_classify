import numpy as np
import sklearn.linear_model as lm
# 模型性能评价模块
import sklearn.metrics as sm
import matplotlib.pyplot as mp
# 管线模块
import sklearn.pipeline as pl
import sklearn.preprocessing as sp


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y=x*2
noise = np.random.uniform(1, 3, size=len(y))
y = y + noise

train_x, train_y = [], []
for i in range(len(x)):
    train_x.append([x[i]])
    train_y.append(y[i])

model = lm.LinearRegression()
model.fit(train_x, train_y)
print(model.coef_)
print(model.intercept_)

print(sm.r2_score(train_y, model.predict(train_x)))

mp.figure("Linear Regression", facecolor="lightgray")
mp.title("Linear Regression", fontsize=20)
mp.xlabel("x", fontsize=14)
mp.ylabel("y", fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=":")
mp.scatter(train_x, train_y, c="dodgerblue", alpha=0.8, s=60, label="Sample")
mp.plot(train_x, model.predict(train_x), c="orangered", label="Pre")
mp.legend()

mp.show()