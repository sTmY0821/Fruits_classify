import jieba
import pandas as pd
import sklearn.svm as svm
from sklearn.feature_extraction.text import CountVectorizer  # 词袋模型向量化对象
from sklearn.metrics import classification_report, accuracy_score

label_map = {0: '负面', 1: '正面'}

# 读取样本
train_data = pd.read_csv('../data/Naive_Bayes/train.tsv', sep='\t')
test_data = pd.read_csv('../data/Naive_Bayes/test.tsv', sep='\t')
# 将读取到的内容赋值给变量
x_train, y_train = train_data.text_a.values, train_data.label.values
x_test, y_test = test_data.text_a.values, test_data.label.values


class SVM_Classifier(object):
    def __init__(self):  # 朴素贝叶斯分类器
        self.model = svm.SVC(kernel='rbf')
        # 使用BOW特征提取
        self.feature_processor = CountVectorizer(tokenizer=jieba.cut)  # 初始化对象，并指定分词器

    def fit(self, x_train, y_train, x_test, y_test):
        # tf-idf特征提取
        x_train_fea = self.feature_processor.fit_transform(x_train)
        # 训练
        self.model.fit(x_train_fea, y_train)

        train_accuracy = self.model.score(x_train_fea, y_train) # 计算平均accuracy
        print("训练集准确率:{}".format(round(train_accuracy, 3)))

        # 测试集提取BOW特征，并执行预测
        x_test_fea = self.feature_processor.transform(x_test)
        y_predict = self.model.predict(x_test_fea)
        test_accuracy = accuracy_score(y_test, y_predict)
        print("测试集准确率:{}".format(round(test_accuracy, 3)))

        # y_predict = self.model.predict(x_test_fea)
        # print("测试集评估:")
        # print(classification_report(y_test, y_predict, target_names=['O', '1']))#打印分类报告

    def single_predict(self, text):
        text_preprocess = [" ".join(jieba.cut(text))] # 分词，将每个词用空格隔开
        text_fea = self.feature_processor.transform(text_preprocess) # 计算BOW特征

        result = self.model.predict(text_fea)
        predict_idx = result[0] # 取出预测结果
        predict_label = label_map[predict_idx] # 将分类结果转换为类别名称
        # predict_proba: 返回属于每个类别的概率
        predict_prob = self.model.predict_proba(text_fea)[0][predict_idx] # 取出概率

        return predict_label, predict_prob # 返回预测结果和概率


if __name__ == "__main__":
    nb_classifier = SVM_Classifier()
    nb_classifier.fit(x_train, y_train, x_test, y_test)

    result, prob = nb_classifier.single_predict("外观很漂亮，出人意料地漂亮，做工非常好")
    print("结果:", result, " 置信度:", prob)

    result, prob = nb_classifier.single_predict("书的内容没什么好说的，主要是纸张、印刷太差，所用的纸非常粗糙比一般的盗版书还要差，裁的也不好。")
    print("结果:", result, " 置信度:", prob)
