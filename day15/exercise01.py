dict_data = {"name":"张三", "age":18,"sex":"男"}
iterator = dict_data.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(f"key:{key} value:{dict_data[key]}")
    except StopIteration:
        break


