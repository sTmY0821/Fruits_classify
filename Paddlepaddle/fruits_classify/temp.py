"""存放公共变量"""
import os

# 数据配置
name_dict = {'apple': 0, 'banana': 1, 'grape': 2, 'orange': 3, 'pear': 4}
name_dict_inv = {v: k for k, v in name_dict.items()}
data_root_path = '../fruits/'
train_file_path = os.path.join(data_root_path, 'train.txt')
test_file_path = os.path.join(data_root_path, 'test.txt')

# 模型参数及超参数
image_size = 224
batch_size = 64
filter_size = 5
num_filters1 = 32
num_filters2 = 64
num_filters3 = 64
pool_size = 2
pool_stride = 2
pool_padding = 0
pool_type = "max"
conv_stride = 1
conv_padding = 0
act = 'relu'
dropout_prob = 0.5
f1_size = 512
fc_act = 'relu'
learning_rate = 0.001
epoch_num= 5

iters = []
costs = []