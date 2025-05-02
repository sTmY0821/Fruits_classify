from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
import sklearn.metrics as sm

# 加载数据集
data = load_diabetes()
X = data.data
y = data.target

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建决策树回归模型
regressor = DecisionTreeRegressor(max_depth=5, random_state=42)

# 训练模型
regressor.fit(X_train, y_train)

# 预测
y_pred = regressor.predict(X_test)

# 评估
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"Mean Absolute Error: {mae}")
print(sm.r2_score(y_test, y_pred))

# 可视化决策树
plt.figure(figsize=(20, 10))
plot_tree(regressor, filled=True, feature_names=data.feature_names, rounded=True)
plt.show()