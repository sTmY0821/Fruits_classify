"""
搭建模型，训练模型，保存模型
"""
import paddle
from click.core import batch

from temp import *
from multiprocessing import cpu_count
import os


#构建数据读取器

def train_mapper(sample):
    label, img_path = sample
    if os.path.exists(img_path):
        #读取图像数据
        img = paddle.dataset.image.load_image(img_path,is_color=True)
        #对图像进行缩放，固定到相同尺寸
        img = paddle.dataset.image.simple_transform(img,
                                                    resize_size=image_size,
                                                    crop_size=image_size,
                                                    is_color=True,
                                                    is_train=True)
        #对图像进行归一化
        img =img.astype('float32')/255.0
        return int(label),img   #img变为了c(通道数）,w,h

def train_r(train_file):
    def reader():
        with open(train_file, 'r')as f:
            for line in f:
                label,img_path =line.strip().split('\t')
                yield label,img_path
    return paddle.reader.xmap_readers(reader=reader,
                                      mapper =train_mapper,
                                      process_num=cpu_count(),
                                      buffer_size=1173)

def test_mapper(sample):
    label, img_path = sample
    if os.path.exists(img_path):
        #读取图像数据
        img = paddle.dataset.image.load_image(img_path,is_color=True)
        #对图像进行缩放，固定到相同尺寸
        img = paddle.dataset.image.simple_transform(img,
                                                    resize_size=image_size,
                                                    crop_size=image_size,
                                                    is_color=True,
                                                    is_train=False)
        #对图像进行归一化
        img =img.astype('float32')/255.0
        return int(label),img   #img变为了c(通道数）,w,h

def test_r(test_file):
    def reader():
        with open(test_file, 'r')as f:
            for line in f:
                label,img_path =line.strip().split('\t')
                yield label,img_path
    return paddle.reader.xmap_readers(reader=reader,
                                      mapper =test_mapper,
                                      process_num=cpu_count(),
                                      buffer_size=133)

#训练集读取器
train_reader = train_r(train_file_path)
train_shuffle_reader=paddle.reader.shuffle(train_reader, buf_size=1173)
train_batch_reader = paddle.batch(train_shuffle_reader, batch_size=batch_size)
#测试集读取器
test_reader = test_r(test_file_path)
test_shuffle_reader=paddle.reader.shuffle(test_reader, buf_size=133)
test_batch_reader = paddle.batch(test_shuffle_reader, batch_size=batch_size)


