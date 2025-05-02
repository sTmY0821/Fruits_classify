"""
匿名函数
    lambda
"""


def func01(a, b):
    return a + b


# 有参数有返回值
fun01 = lambda a, b: a + b
print(fun01(1, 2))
# 没有参数有返回值
fun02 = lambda: 250
# 有参数没有返回值
fun03 = lambda a: print("参数是%s"%a)
# 没有参数没有返回值
fun04 = lambda: print("无参数无返回值")

#lambda函数不支持赋值语句,且lambda函数只能有一条语句