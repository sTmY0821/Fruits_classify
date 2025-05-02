from day17.common import  iterable_tools
"""

"""
dict01 = {
    "name":"张三",
    "age":18,
    "gender":"男",
    "address":"北京",
    "phone":"18200115208"
}


def condition_key_18(item):
    return item[1] == 18

def condition_key_str(item):
    return type(item[1]) == str

print(iterable_tools.IterableHelper.find_single(dict01.items(),lambda item:item[1] == 18))

for item in iterable_tools.IterableHelper.find_everything(dict01.items(),lambda item01:type(item01[1])==str):
    print(item[0])
