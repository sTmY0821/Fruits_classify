from bll import RestaurantController
from usl import RestaurantModel


class RestaurantView:
    def __init__(self):
        self.controller = RestaurantController()

    def display_menu(self):
        print("1. 显示所有餐厅")
        print("2. 添加餐厅")
        print("3. 删除餐厅")
        print("4. 修改餐厅")
        print("5. 退出系统")

    def select_menu(self):
        number = int(input("请输入选项："))
        if number == 1:
            self.display_restaurants()
        elif number == 2:
            self.input_restaurant()
        elif number == 3:
            self.delete_restaurant()
        elif number == 4:
            self.modify_restaurant()
        elif number == 5:
            exit()
        else:
            print("输入错误，请重新输入")

    def display_restaurants(self):
        for item in self.controller.restaurant_list:
            print(item)

    def input_restaurant(self):
        model = RestaurantModel(input("请输入餐厅名称"), input("请输入餐厅所在城市"),
                                int(input("请输入人均消费")))
        self.controller.add_restaurant(model)

    def delete_restaurant(self):
        name = input("请输入要删除的餐厅名称：")
        if self.controller.remove_restaurant(name):
            print("删除成功")
        else:
            print("删除失败")

    def modify_restaurant(self):
        name = input("请输入要修改的餐厅名称：")
        model = RestaurantModel(input("请输入餐厅名称"), input("请输入餐厅所在城市"),
                                int(input("请输入人均消费")))
        if self.controller.modify_restaurant(name, model):
            print("修改成功")
        else:
            print("修改失败")
