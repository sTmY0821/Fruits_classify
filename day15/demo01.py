"""
迭代器具有__next__()方法

"""


class MyRange:
    def __init__(self, number: int):
        self.number = number
        self.index = -1

    def __iter__(self):
        self.index += 1
        yield self.index
        self.index += 1
        yield self.index
        self.index += 1
        yield self.index
        self.index += 1
        yield self.index


i = MyRange(3)
iterator = i.__iter__()
item = iterator.__next__().__next__()
print(item)

