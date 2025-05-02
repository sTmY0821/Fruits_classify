"""
文件读写的应用

练习：day14 epidemic
"""

class RestaurantModel:
    def __init__(self,name,city,money):
        self.name = name
        self.city = city
        self.money = money
    # 对人类友好，没有格式限制，用于展示给人看
    def __str__(self):
        return "%s餐厅位于%s，人均消费%s元"%(self.name,self.city,self.money)
    #对机器友好，语法格式限制，创建对象时的格式，用于展示给机器看
    def __repr__(self):
        return 'RestaurantModel("%s","%s",%s)'%(self.name,self.city,self.money)
#内存对象
list_table=[RestaurantModel("老北京烤鸭","北京",100),
            RestaurantModel("蟹黄面","上海",20),
            RestaurantModel("张姐火锅","成都",200),
]
#写入到文件
with open("restaurant.txt","w",encoding="utf-8") as file:
    file.write(list_table.__repr__())
#从文件读取回内存
with open("restaurant.txt", "r", encoding="utf-8") as file:
    m2 =eval(file.read())
    print(m2)