# 创建疫情类型
class Restaurant:
    def __init__(self, name, city, pre_consumption):
        self.name = name
        self.city = city
        self.pre_consumption = pre_consumption

    def display(self):
        print("%s位于%s，人均消费为%s元" % (self.name, self.city, self.pre_consumption))


# 定义显示菜单函数
def display_menu():
    print("按1选择增加餐厅")
    print("按2选择查询餐厅")
    print("按3选择删除餐厅")
    print("按3选择修改餐厅")


# 定义选择菜单
def select_menu(number):
    if number == "1":
        add_restaurant()
    elif number == "2":
        display_restaurant()
    elif number == "3":
        delete_restaurant()
    elif number == "4":
        modify_restaurant()
    else:
        return True


# 定义增加函数
def add_restaurant():
    add_rest = Restaurant(input("请输入餐厅名称"), input("请输入餐厅所在城市"), int(input("请输入人均消费")))
    list_restaurant.append(add_rest)


# 定义查询函数
def display_restaurant():
    for i in range(len(list_restaurant)):
        list_restaurant[i].display()
        

# 定义删除函数
def delete_restaurant():
    del_name = input("请输入要删除的餐厅名称")
    for i in range(len(list_restaurant)):
        if del_name == list_restaurant[i].name:
            del list_restaurant[i]
            break


# 定义修改干数
def modify_restaurant():
    modi_name = input("请输入要修改的餐厅名称")
    for i in range(len(list_restaurant)):
        if modi_name == list_restaurant[i].name:
            new_restaurant = Restaurant(input("请输入餐厅名称"), input("请输入餐厅所在城市"),
                                        int(input("请输入人均消费")))
            list_restaurant[i] = new_restaurant
            break


# ——————————程序入口——————————————
list_restaurant = []
while True:
    display_menu()
    select_menu(input("请输入数字选择您的需求"))
