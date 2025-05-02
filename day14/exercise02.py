from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# 示例：文本分类
corpus = [
    'This is a positive review',
    'This is a negative review',
    'Another positive comment',
    'Negative feedback here'
]
labels = np.array([1, 0, 1, 0])  # 1: 正面，0: 负面

# 文本向量化（词袋模型）
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

# 训练模型
model = MultinomialNB(alpha=1.0)  # 拉普拉斯平滑
model.fit(X, labels)

# 预测新样本
new_text = ['You look great']
X_new = vectorizer.transform(new_text)
print(model.predict(X_new))  # 输出: [1]