"""
循环神经网络
"""
import numpy as np

w_xh = 0.5
w_hh = 0.8
b_h = 0.1

def tanh(x):
    return np.tanh(x)

#输入序列
x= [1.0,2.0,3.0]
h = 0.0
hidden_state = []
for i in x:
    h = tanh(w_xh*i + w_hh*h + b_h)
    hidden_state.append(h)
print(hidden_state)