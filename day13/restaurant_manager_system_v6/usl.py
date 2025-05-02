class RestaurantModel:
    def __init__(self, name: str="", city: str="", avg_price: float=0):
        self.name = name
        self.city = city
        self.avg_price = avg_price
    def __str__(self):
        return "名称：%s位于%s，平均价格：%s" % (self.name, self.city, self.avg_price)

    def __eq__(self, other):
        return self.name == other.name