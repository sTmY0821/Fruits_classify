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



print(IterableHelper.get_max(list_table, lambda movie: movie.score))
print(IterableHelper.get_min(list_table, lambda movie: movie.score))
IterableHelper.sort_from_big_small(list_table, lambda movie: movie.score)
for item in list_table:
    print(item.__dict__)