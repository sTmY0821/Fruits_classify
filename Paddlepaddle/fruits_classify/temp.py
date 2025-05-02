"""存放公共变量"""
import os


#数据配置
name_dict = {'apple':0,'banana':1,'grape':2,'orange':3,'pear':4}
name_dict_inv = {v:k for k,v in name_dict.items()}
data_root_path = '../fruits/'
train_file_path = os.path.join(data_root_path,'train.txt')
test_file_path = os.path.join(data_root_path,'test.txt')


#模型参数及超参数
image_size = 224
batch_size = 64