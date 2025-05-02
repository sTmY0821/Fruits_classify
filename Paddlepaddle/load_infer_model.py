# 波士顿放假预测
import os.path

import paddle.fluid as fluid
import numpy as np
import matplotlib.pyplot as plt
import paddle


# 数据准备


test_reader = paddle.dataset.uci_housing.test()
test_batch_reader = paddle.batch(test_reader, batch_size=2)
test_data = next(test_batch_reader())
# infer_reader = paddle.batch(paddle.dataset.uci_housing.test(),
#                             batch_size=2)  # 测试数据读取器
# test_data = next(infer_reader())  # 获取一条数据
test_x = np.array([data[0] for data in test_data], dtype='float32')
test_y = np.array([data[1] for data in test_data], dtype='float32')
#infer_exe执行program，把待预测数据传入 feed_target_names中，从fetch_targets中得到预测结果
place = fluid.CPUPlace()
infer_exe = fluid.Executor(place)
infer = fluid.io.load_inference_model('model/boston/infer/', infer_exe)
# [infer_program, feed_target_names, fetch_targets] = fluid.io.load_inference_model('model/boston/infer/',  # 模型保存路径
#                                   infer_exe)  # 要执行模型的Executor
x_name = infer[1][0]
result = infer_exe.run(infer[0],feed = {x_name: test_x},fetch_list=infer[2])
print(result)