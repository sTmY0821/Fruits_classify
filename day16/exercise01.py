list01 = [
    {"name": "张三", "age": 27}
    , {"name": "李四", "age": 21}
    ,{"name": "王五", "age": 20}
]

def find_age():
    for iterm in list01:
        if iterm["age"] > 20:
            yield iterm

for name in find_age():
    print(name)