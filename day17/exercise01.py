"""
1.根据需求写出函数
    在电影列表中累加所有的电影评分
    在电影列表中累加所有的电影年份
2.定义高阶函数，通过lambda函数实现相同功能
3.将高阶函数封装到IterableHelper当中
"""

import day17.common.iterable_tools as it

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
    MovieModel("阿甘正传", 1994, 9.6),
    MovieModel("美丽人生", 1997, 9.5),
    MovieModel("千与千寻", 2001, 9.6),
    MovieModel("辛德勒的名单", 1993, 9.5),
]
def get_score(movie):
    return movie.score

def get_year(movie):
    return movie.year

def add_number(condition):
    return sum(condition(movie) for movie in list_table)

print(add_number(get_score))
print(add_number(get_year))
print(add_number(lambda movie:movie.score))
print(add_number(lambda movie:movie.year))
print(it.IterableHelper.accumulate(list_table,lambda movie:movie.score))
print(it.IterableHelper.accumulate(list_table,lambda movie:movie.year))


