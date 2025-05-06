from PIL import Image
import paddle.fluid as fluid
import paddle
from temp import *
import numpy as np
import os
import matplotlib.pyplot as plt
import keyboard

#定义执行器
place = fluid.CPUPlace()
infer_exe = fluid.Executor(place)

#加载模型
# infer_program, feed_target_names, fetch_targets =\
#     fluid.io.load_inference_model(model_infer_path,
#                                   infer_exe))
infer_program, \
feed_target_names, \
fetch_targets = fluid.io.load_inference_model(model_infer_path, infer_exe)

#加载数据
def load_img(path):
    img = paddle.dataset.image.load_and_transform(path,image_size,image_size,False).astype('float32')
    img = img/255.0
    return img
infer_imgs = []
img_list = os.listdir(test_img_path)
for img in img_list:
    img_path = os.path.join(test_img_path,img)
    infer_imgs.append(load_img(img_path))
infer_imgs = np.array(infer_imgs)
#预测
results = infer_exe.run(infer_program,
                       feed={feed_target_names[0]: infer_imgs},
                       fetch_list=fetch_targets)
print(results)
pred_y = np.argmax(results[0],  axis=1)
pred_x = np.max(results[0], axis=1)
for i in range(len(pred_y)):
    print(f'当前图像：{img_list[i]}, 预测结果：{name_dict_inv[pred_y[i]]},预测概率：{pred_x[i]}')
    img = Image.open(os.path.join(test_img_path,img_list[i]))
    plt.imshow(img)
    plt.show()
    # print("请按空格键查看下一张图像...")
    # keyboard.wait('space')  # 等待按下空格
    # print("已切换到下一张图像")
