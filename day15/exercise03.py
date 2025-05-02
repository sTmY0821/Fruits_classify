
class MyRange:
    def __init__(self, number: int):
        self.number = number

    def __iter__(self):
        return MyRangeIterator(self.number)


class MyRangeIterator:
    def __init__(self, number):
        self.number = number
        self.index = -1

    def __next__(self):
        self.index += 1
        if self.index < self.number:
            return self.index
        else:
            raise StopIteration


i = MyRange(10)
iter = i.__iter__()
while True:
    try:
        item = iter.__next__()
        print(item)
    except StopIteration:
        break
