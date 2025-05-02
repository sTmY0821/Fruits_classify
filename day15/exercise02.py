class BookIterator:
    def __init__(self,data):
        self.data = data
        self.index = -1

    def __next__(self):
        self.index += 1
        if self.index >= len(self.data):
            raise StopIteration # 发送错误消息
            # return 正确结果
        return self.data[self.index]

class BookController:
    def __init__(self):
        self.list_table = []

    def __iter__(self):
        return BookIterator(self.list_table)

controller = BookController()
controller.list_table.append("西游记")
controller.list_table.append("红楼梦")
controller.list_table.append("三国")
# for item in controller:
#     print(item)
iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break