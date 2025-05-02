#关键词提取
import math
import jieba
from jieba import analyse



#停用词加载方法
def get_stop_words():
    stop_words = []
    with open("NLP_DATA/stop_words.utf8", "r", encoding="utf-8") as f:
        lines = f.readlines()
    stopwords_list = [sw.replace("\n", "") for sw in lines]
    return stopwords_list

#去掉停用次
def word_filter(seg_list):
    filter_list = []
    for word in seg_list:
        if word not in get_stop_words() and len(word) > 1 :
            filter_list.append(word)
    return filter_list


#数据加载
def load_data(corpus_path):
    doc_list = []
    for line in open(corpus_path, "r", encoding="utf-8"):
        content = line.strip()#去掉换行符
        seg_list = jieba.cut(content)
        filter_list =word_filter(seg_list)
        doc_list.append(filter_list)
    return doc_list

#idf值统计方法
def train_idf(doc_list):
    idf_dic = {}
    tt_count = len(doc_list)
    for doc in doc_list:
        doc_set = set(doc)
        for word in doc_set:
            if word not in idf_dic:
                idf_dic[word] = 1
            else:
                idf_dic[word] += 1
    for word,doc_cnt in idf_dic.items():
        idf_dic[word] = math.log(tt_count / (doc_cnt + 1))
    default_idf = math.log(tt_count / 1)
    return idf_dic,default_idf

#TF-IDF类
class Tfidf:
    def __init__(self,idf_dic,default_idf,word_list,keyword_num):
        self.word_list = word_list
        self.idf_dic = idf_dic
        self.default_idf = default_idf
        self.tf_dic = self.get_tf_dic()
        self.keyword_num = keyword_num
    def get_tf_dic(self):
        tf_dic = {}
        for word in self.word_list:
            tf_dic[word] = tf_dic.get(word,0.0)+1
        total =len(self.word_list)
        for word,word_cnt in tf_dic.items():
            tf_dic[word] = float(word_cnt/total)
        return tf_dic
    def get_tfidf(self):
        tfidf_dic = {}
        for word in self.word_list:
            idf = self.idf_dic.get(word,self.default_idf) #获取idf值
            tf = self.tf_dic.get(word,0) #获取词频

            tfidf = tf * idf
            tfidf_dic[word] = tfidf
        s_list = sorted(tfidf_dic.items(),key=lambda x:x[1],reverse=True)
        print(s_list)
        top_list = s_list[:self.keyword_num]
        for k,v in top_list:
            print(k+",",end = " ")


def tfidf_extract(word_list,keyword_num =20):
    doc_list = load_data("NLP_DATA/keywords_extract/corpus.txt")
    print(doc_list)
    idf_dic,default_idf = train_idf(doc_list)
    tfidf_model = Tfidf(idf_dic,default_idf,word_list,keyword_num)
    tfidf_model.get_tfidf()

def text_extract(text,keyword_num =20):
    keywords = analyse.textrank(text,keyword_num)
    for k in keywords:
        print(k+",",end = "")

if __name__ == "__main__":
    global stopword_list
    text = """在中国共产党百年华诞的重要时刻，在“两个一百年”奋斗目标历史交汇关键节点，
        党的十九届六中全会的召开具有重大历史意义。全会审议通过的《决议》全面系统总结了党的百年奋斗
        重大成就和历史经验，特别是着重阐释了党的十八大以来党和国家事业取得的历史性成就、发生的历史性变革，
        充分彰显了中国共产党的历史自觉与历史自信。"""

    stopword_list = get_stop_words()
    seg_list = jieba.cut(text)
    filter_list = word_filter(seg_list)
    # TF-IDF提取关键词
    print('TF-IDF模型结果：')
    tfidf_extract(filter_list)
    print('TEXTRANK模型结果：')
    text_extract(text)
