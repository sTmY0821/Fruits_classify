import numpy as np
import sklearn.linear_model as lm
import pickle
import matplotlib.pyplot as mp

x = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 3, 5, 7, 9])

with open('linear_model.pkl', 'rb')as f:
    model = pickle.load(f)

pred_y = model.predict(x)

mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.grid(linestyle=':')
mp.scatter(x, y, c='dodgerblue', alpha=0.8, s=60, label='Sample')
mp.plot(x, pred_y, c='orangered', label='Predict')
mp.tick_params(labelsize=10)
mp.legend('upper-right')

mp.show()

