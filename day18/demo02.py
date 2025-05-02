"""
内置高阶函数

"""
from day17.common.iterable_tools import IterableHelper


class MovieModel:
    def __init__(self, name: str, year: int, score: float):
        self.name = name
        self.year = year
        self.score = score

    def __str__(self):
        return "电影名称:{0},上映年份:{1},评分:{2}".format(self.name, self.year, self.score)


list_table = [
    MovieModel("肖申克的救赎", 1994, 9.6),
    MovieModel("霸王别姬", 1993, 9.5),
    MovieModel("阿甘正传", 1994, 9.7),
    MovieModel("美丽人生", 1997, 9.5),
    MovieModel("千与千寻", 2001, 9.3),
    MovieModel("辛德勒的名单", 1993, 9.4),
]
# 1.过滤器：筛选出满足条件的元素，类似于for循环，但是返回的是一个迭代器
for item in filter(lambda movie: movie.year > 1995, list_table):
    print(item)

# 2.最大最小(命名关键字形参)
print(max(list_table, key=lambda movie: movie.year))

# 3.排序：升序降序
list_table.sort(key=lambda movie: movie.year)
list_table.sort(key=lambda movie: movie.year, reverse=True)
for item in list_table:
    print(item)
# 对任意可迭代对象进行排序，返回列表
sorted_list = sorted(list_table, key=lambda movie: movie.year, reverse=False)
for item in sorted_list:
    print(item)

# 4.获取所有电影名
map(lambda movie: movie.name, list_table)  # map的意思为映射
for item in map(lambda movie: movie.name, list_table):
    print(item)
