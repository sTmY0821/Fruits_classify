
class RestaurantModel:
    def __init__(self, name: str, city: str, avg_price: float):
        self.name = name
        self.city = city
        self.avg_price = avg_price

    def display_restauraunt(self):
        print("%s餐厅位于%s，人均消费%s元" % (self.name, self.city, self.avg_price))


class RestaurantView:
    def __init__(self):
        self.controller = RestaurantController()

    def display_menu(self):
        print("按1选择增加餐厅")
        print("按2选择查询餐厅")
        print("按3选择删除餐厅")
        print("按4选择修改餐厅")

    def select_menu(self):
        number = input("请输入数字选择操作")
        if number == "1":
            self.controller.add_restaurant(self.input_restaurant())
        elif number == "2":
            self.display_restaurants()
        elif number == "3":
            self.delete_restaurant()
        elif number == "4":
            self.modify_restaurant()
        else:
            return True

    def input_restaurant(self):
        new_restaurant = RestaurantModel(
            name=input("请输入餐厅名"),
            city=input("请输入餐厅所在城市"),
            avg_price=input("请输入餐厅人均消费"))
        return new_restaurant

    def display_restaurants(self):
        for restaurant in self.controller.restaurant_list:
            restaurant.display_restauraunt()

    def delete_restaurant(self):
        name = input("请输入要删除的餐厅名称")
        if self.controller.remove_restaurant(name):
            print("删除成功")
        else:
            print("删除失败")
    def modify_restaurant(self):
        name = input("请输入要修改的餐厅名称")
        for restaurant in self.controller.restaurant_list:
            if restaurant.name == name:
                restaurant.name = input("请输入修改后的餐厅名称")
                restaurant.city = input("请输入修改后的餐厅所在城市")
                restaurant.avg_price = input("请输入修改后的餐厅人均消费")
                print("修改成功")
                return True
            else:
               print("修改失败")



class RestaurantController:
    def __init__(self):
        self.restaurant_list = []

    def add_restaurant(self,model)->None:
        self.restaurant_list.append(model)

    def remove_restaurant(self,name)->bool:
        for i in range(len(self.restaurant_list)):
            if self.restaurant_list[i].name == name:
                del self.restaurant_list[i]
                return True
            else:
                return False


view = RestaurantView()
while True:
    view.display_menu()
    view.select_menu()