import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms
import matplotlib.pyplot as mp

data = []
with open('../data/car.txt', 'r') as f:
    for line in f.readlines():
        data.append(line.replace('\n', '').split(','))

data = np.array(data).T
encoders,train_x = [],[]
for row in range(len(data)):
    encoder = sp.LabelEncoder()
    encoders.append(encoder)
    if row < len(data) - 1:
        train_x.append(encoder.fit_transform(data[row]))
    else:
        train_y = encoder.fit_transform(data[row])

train_x = np.array(train_x).T

model = se.RandomForestClassifier(max_depth= 8,random_state=7)

n_estimators = np.array(50,550,50)
train_scores1,test_scores1 = ms.validation_curve(model,train_x,train_y,
                                                  'n_estimators',n_estimators,
                                                  cv=5)
train_mean = train_scores1.mean(axis=1)#按行求均值
print("train_mean:", train_mean)
test_mean = test_scores1.mean(axis=1)
print("test_mean:", test_mean)


