
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

def condition_four_name(movie: MovieModel):
    return len(movie.name)==4


print(IterableHelper.find_single(list_table, condition_four_name).__dict__)
for iterm in IterableHelper.find_everything(list_table, condition_four_name):
    print(iterm.__dict__)
