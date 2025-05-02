# 决策树回归示例
# 使用决策树预测波士顿房价

import sklearn.datasets as sd #读取数据集
import sklearn.utils as su #通用函数模块
import sklearn.tree as st #决策树模块
import sklearn.ensemble as se #集成学习模块
import sklearn.metrics as sm #计算模型的指标


boston = sd.load_boston()  # 加载boston地区房价数据
print(boston.feature_names) #打印特征名称
print(boston.data.shape)
print(boston.target.shape)

random_seed = 7  # 随机种子，计算随机值，相同的随机种子得到的随机值一样
x, y = su.shuffle(boston.data,
                  boston.target,
                  random_state = random_seed)
# 计算训练数据的数量
train_size = int(len(x) * 0.8) # 以boston.data中80%的数据作为训练数据
# 构建训练数据、测试数据
train_x = x[:train_size]  # 训练输入, x前面80%的数据
test_x = x[train_size:]   # 测试输入, x后面20%的数据
train_y = y[:train_size]  # 训练输出
test_y = y[train_size:]   # 测试输出

######## 单棵树进行预测 ########
# 模型
model = st.DecisionTreeRegressor(max_depth=4)  # 决策回归器

# 训练
model.fit(train_x, train_y)
# 预测
pre_test_y = model.predict(test_x)
# 打印预测输出和实际输出的R2值
print(sm.r2_score(test_y, pre_test_y))

import matplotlib.pyplot as mp
import numpy as np
fi = model.feature_importances_  # 获取特征重要性
print("fi:", fi)

# 特征重要性可视化
mp.figure("Feature importances", facecolor="lightgray")
mp.plot()
mp.title("DT Feature", fontsize=16)
mp.ylabel("Feature importances", fontsize=14)
mp.grid(linestyle=":")
x = np.arange(fi.size)
sorted_idx = fi.argsort()[::-1]  # 重要性排序(倒序)
fi = fi[sorted_idx]  # 根据排序索引重新排特征值
mp.xticks(x, boston.feature_names[sorted_idx])
mp.bar(x, fi, 0.4, color="dodgerblue", label="DT Feature importances")

mp.legend()
mp.tight_layout()
mp.show()

