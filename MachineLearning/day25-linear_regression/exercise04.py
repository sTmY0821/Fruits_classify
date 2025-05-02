import numpy as np
import matplotlib.pyplot as mp
import sklearn.metrics as sm
import sklearn.linear_model as lm

advertising_investment = np.array([[230.1],
                                   [44.5],
                                   [17.2],
                                   [151.5],
                                   [180.8],
                                   [57.5],
                                   [120.2],
                                   [8.6]])
# advertising_investment = np.array([230.1,
#                                    44.5,
#                                    17.2,
#                                    151.5,
#                                    180.8,
#                                    57.5,
#                                    120.2,
#                                    8.6])
revenue_sales = np.array([22.1, 10.4, 9.3, 18.5, 12.9, 11.8, 13.2, 4.8])
#三板斧：定义模型、训练模型、预测/评估模型
#定义模型
model = lm.LinearRegression()#线性回归模型
#训练模型
model.fit(advertising_investment, revenue_sales)#回归为有监督，需要传入、标签
#预测/评估模型
prey_revenue = model.predict(advertising_investment)#预测
print('斜率：', model.coef_)
print('截距：', model.intercept_)

mp.figure('Linear Regression',facecolor='lightgray')
mp.title('Linear Regression',fontsize=16)
mp.xlabel('advertising_investment',fontsize=14)
mp.ylabel('revenue_sales',fontsize=14)
mp.grid(linestyle=':')
mp.tick_params(labelsize=10)
mp.scatter(advertising_investment,revenue_sales,c='blue',alpha = 0.8,s=60,label='Sample')
mp.plot(advertising_investment,prey_revenue,c='red',label='Regression')

mp.legend()
mp.show()

print('R2:',sm.r2_score(revenue_sales,prey_revenue))
print("advertising 300:", model.predict([[300]]))
print("advertising 400:", model.predict([[400]]))
print("advertising 500:", model.predict([[500]]))


