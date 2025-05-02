import numpy as np
import sklearn.linear_model as lm
import pickle

x = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 2, 3, 4, 5])

model = lm.LinearRegression()
model.fit(x, y)

with open("linear_model.pkl","wb")as f:
    pickle.dump(model,f)
    print("模型保存成功")

