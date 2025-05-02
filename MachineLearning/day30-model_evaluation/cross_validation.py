# 交叉验证示例
import numpy as np
import sklearn.model_selection as ms
import sklearn.naive_bayes as nb
import matplotlib.pyplot as mp

x, y = [], []  # 输入，输出

# 读取数据文件
with open("../data/multiple1.txt", "r") as f:
    for line in f.readlines():
        data = [float(substr) for substr in line.split(",")]
        x.append(data[:-1])  # 输入样本：取从第一列到导数第二列
        y.append(data[-1])  # 输出样本：取最后一列

train_x = np.array(x)
train_y = np.array(y, dtype=int)

# 划分训练集和测试集
#train_x, test_x, train_y, test_y = ms.train_test_split(
#    x, y, test_size=0.25, random_state=7)

# 创建高斯朴素贝叶斯分类器对象
model = nb.GaussianNB()
# 先做交叉验证，如果得分结果可以接受，再执行训练和预测
pws = ms.cross_val_score(model, x, y,
                         cv=5,  # 折叠数量
                         scoring='precision_weighted')  # 查准率
print("precision:", pws.mean())

rws = ms.cross_val_score(model, x, y, cv=5,
                         scoring='recall_weighted')  # 召回率
print("recall:", rws.mean())

f1s = ms.cross_val_score(model, x, y, cv=5,
                         scoring='f1_weighted')  # F1得分
print("f1:", f1s.mean())

acc = ms.cross_val_score(model, x, y,
                         cv=5, scoring='accuracy')  # 准确率
print("acc:", acc.mean())