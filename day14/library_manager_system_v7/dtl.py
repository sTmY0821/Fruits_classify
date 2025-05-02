class LibraryModel:
    def __init__(self, name: str="", publisher: str= "", price: float=0):
        self.name = name
        self.publisher = publisher
        self.price = price

    def __str__(self):
        return "书名：%s，出版社：%s，价格：%.2f" % (self.name, self.publisher, self.price)

    def __eq__(self, other):
        return self.name == other.name