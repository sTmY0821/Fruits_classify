import jieba
import jieba.posseg as psg
text = "吉林市长春药店"

seg_list = jieba.cut(text,cut_all=False)
print("/".join(seg_list))

def pos(text):
    results = psg.cut(text)
    for word,flag in results:
        print("%s/%s"%(word,flag),end=" ")


pos("呼伦贝尔大草原")