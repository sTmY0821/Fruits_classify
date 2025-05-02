from temp import *
import os


#记录每个类别下的图片
result_dict = {'apple':[],'banana':[],'grape':[],'orange':[],'pear':[]}

#遍历子目录,拼接每张图片的完整路径
dirs=os.listdir(data_root_path)
for d in dirs:
    sub_dirs = os.path.join(data_root_path,d)
    if os.path.isdir(sub_dirs):
        imgs = os.listdir(sub_dirs)
        for img in imgs:
            all_path =os.path.join(sub_dirs,img)
            if d not in result_dict.keys():
                result_dict[d] = []
            result_dict[d].append(all_path)

#清空和创建文件
with open(train_file_path,'w')as f:
    pass
with open(test_file_path,'w')as f:
    pass

#划分训练集和测试集
for name,img_list in result_dict.items():
    print(name,len(img_list))
    with open(train_file_path,'a')as f:
        for img in img_list[:int(len(img_list)*0.9)]:
            f.write(str(name_dict[name])+'\t'+img+'\n')
    with open(test_file_path,'a')as f:
        for img in img_list[int(len(img_list)*0.9):]:
            f.write(str(name_dict[name])+'\t'+img+'\n')
