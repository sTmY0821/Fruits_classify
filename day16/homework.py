"""
定义函数1:在电影列表中查找“霸王别姬”的model对象
定义函数2:在电影列表中查找第一个1997年上映的model 对象
定义函数3:在电影列表中查找第一个分数大于9.5的model对象
要求使用函数式编程思想
"""

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

def condition01(movie: MovieModel):
    return movie.name == "霸王别姬"

def condition02(movie: MovieModel):
    return movie.year == 1997

def condition03(movie: MovieModel):
    return movie.score > 9.5

def find_movie(condition):
    for movie in list_table:
        if condition(movie):
            return movie
        else:
            continue

print(find_movie(lambda item:item.name == "霸王别姬"))
print(find_movie(lambda item:item.year == 1997))
print(find_movie(lambda item:item.score > 9.5))




