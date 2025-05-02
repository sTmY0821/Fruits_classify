"""
生成器表达式
    将列表推导式的中括号变为小括号即可
    即使产生大量数据也几乎不占内存

    面试题：何时使用列表？何时使用生成器？
"""
list01= ["孙悟空", "猪八戒", "沙僧", "唐僧"]
def get_name():
    for name in list01:
        if len(name) ==2:
            yield name

for name in get_name():
    print(name)

def get_name_2():
    for name in list01:
        if len(name) ==2:
            return name
            break

print(get_name_2())

