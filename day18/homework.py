from day17.common.iterable_tools import IterableHelper
class RestaurantModel:
    def __init__(self,name,city,money):
        self.name = name
        self.city = city
        self.money = money
    def __str__(self):
        return "%s餐厅位于%s，人均消费%s元"%(self.name,self.city,self.money)

list_table = [
    RestaurantModel("餐厅A","北京",20),
    RestaurantModel("餐厅B","深圳",30),
    RestaurantModel("餐厅C","广州",40),
    RestaurantModel("餐厅D","深圳",50),
    RestaurantModel("餐厅E","杭州",60)
]


for item in filter(lambda restaurant:restaurant.money>40,list_table):
    print(item.__dict__)

print(min(list_table,key=lambda restaurant:restaurant.money).__dict__)

for item in map(lambda restaurant:restaurant.name,list_table):
    print(item)

descending_sort =sorted(list_table,key =lambda restaurant:restaurant.money,reverse=True)
for item in descending_sort:
    print(item.__dict__)

print(IterableHelper.if_same_attribute(list_table,lambda restaurant:restaurant.city))
print(IterableHelper.if_same_attribute(list_table,lambda restaurant:restaurant.name))