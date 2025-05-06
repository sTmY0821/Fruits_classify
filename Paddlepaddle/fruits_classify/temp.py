"""存放公共变量"""
import os

# 数据配置
name_dict = {'apple': 0, 'banana': 1, 'grape': 2, 'orange': 3, 'pear': 4}
name_dict_inv = {v: k for k, v in name_dict.items()}
data_root_path = '../fruits/'
train_file_path = os.path.join(data_root_path, 'train.txt')
test_file_path = os.path.join(data_root_path, 'test.txt')
model_train_path = '../model/fruits/train'
model_infer_path = '../model/fruits/infer'
vgg_train_path = '../model/fruits/vgg_train'
vgg_infer_path = '../model/fruits/vgg_infer'
test_img_path = './test_img'

# 模型参数及超参数
image_size = 224
batch_size = 64
filter_size = 3
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
fc_size = 512
fc_act = 'relu'
learning_rate = 0.001
epoch_num= 20

#VGG模型参数配置
vgg_params={
    'pool_size':2,
    'pool_stride':2,
    'conv_filter_size':3,
    'conv_act':'relu',
    'pool_type':"max",
    'conv_padding':1
}

iters = []
costs = []