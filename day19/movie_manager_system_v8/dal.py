class MovieDao:
    """
    数据访问对象
    """
    def __init__(self):
        self.file_name = "movie.txt"
    """
    将内存中的列表存入文件
    """
    def save(self,data):
        with open(self.file_name, "w", encoding="utf-8") as file:
            file.write(data.__repr__())

    """
    将文件中的数据串
    """
    def load(self):
        try:
            with open (self.file_name, "r", encoding="utf-8") as file:
                return eval(file.read())
        except FileNotFoundError:
            return []#没有历史文件，返回空列表

