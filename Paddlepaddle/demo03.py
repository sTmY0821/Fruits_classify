import paddle.fluid as fluid
import numpy as np

x= fluid.layers.data(name='x',shape=[1,3],dtype='float32')

w = fluid.layers.create_parameter(shape=[3,4],dtype='float32')
b = fluid.layers.create_parameter(shape=[4],dtype='float32',is_bias=True)

prey_y = fluid.layers.matmul(x,w) + b
place = fluid.CPUPlace()
exe = fluid.Executor(place)
exe.run(fluid.default_startup_program())
x_data = np.arange(1,4).reshape(1,3).astype('float32')
out = exe.run(fluid.default_main_program(),
             feed={'x':x_data},
             fetch_list=[prey_y])

print(out[0])
