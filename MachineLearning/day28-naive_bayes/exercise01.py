import numpy as np
import sklearn.naive_bayes as nb
import matplotlib.pyplot as plt

x, y = [], []

with open("../data/multiple1.txt", "r") as f:
    for line in f.readlines():
        data = [float(i) for i in line.split(",")]
        x.append(data[:-1])
        y.append(data[-1])
x = np.array(x)
y = np.array(y)

model = nb.GaussianNB()
model.fit(x, y)

left = x[:, 0].min() - 1
right = x[:, 0].max() + 1
top = x[:, 1].max() + 1
bottom = x[:, 1].min() - 1

grid_x, grid_y = np.meshgrid(np.arange(left, right, 0.01), np.arange(bottom, top, 0.01))

mesh_x = np.column_stack((grid_x.ravel(), grid_y.ravel()))
mesh_z = model.predict(mesh_x)
mesh_z = mesh_z.reshape(grid_x.shape)

plt.figure("Naive Bays Classification", facecolor="lightgray")
plt.title("Naive Bays Classification", fontsize=16)
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)
plt.tick_params(labelsize=10)
plt.pcolormesh(grid_x, grid_y, mesh_z, cmap='gray')
plt.scatter(x[:, 0], x[:, 1], c=y, cmap='brg',s= 80)
plt.show()
