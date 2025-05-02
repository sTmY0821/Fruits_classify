"""
创建电影列表生成器
"""
class MovieController:
    def __init__(self):
        self.list_table = []
    def __iter__(self):
        return MovieIterator(self.list_table)

class MovieIterator:
    def __init__(self, data):
        self.data = data
        self.index = -1
    def __next__(self):
        self.index += 1
        if self.index >= len(self.data):
            raise StopIteration
        return self.data[self.index]



controller = MovieController()
controller.list_table.append("西游记")
controller.list_table.append("红楼梦")
controller.list_table.append("三国")
iterator = controller.__iter__()
while True:
    try:
        movie =iterator.__next__()
        print(movie)
    except StopIteration:
        break