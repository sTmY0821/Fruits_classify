"""
执行两个张量的相加
"""

import paddle.fluid as fluid

x = fluid.layers.fill_constant(shape=(1,),dtype='float32',value=100.0)
y = fluid.layers.fill_constant(shape=(1,),dtype='float32',value=200.0)
result = x+y
exe = fluid.Executor(fluid.CPUPlace())
exe.run(program=fluid.default_startup_program())
out = exe.run(program=fluid.default_main_program(),fetch_list=[result])
print(out)

