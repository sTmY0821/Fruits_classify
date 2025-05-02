"""
软件架构（重点学习分工）
    视图（view）                     控制器（controller）
    输入、输出                       存储、计算
"""
from day07.homework import input_book


# 创建疫情类型
class BookModel:
    """
    数据类型
    """

    def __init__(self, name, price, publisher):
        self.name = name
        self.price = price
        self.publisher = publisher

    def display(self):
        print("%s书本的单价为%s，出版社是%s" % (self.name, self.price, self.publisher))


class BookView:
    """
    视图：负责界面逻辑，输入输出
    """

    def __init__(self):
        self.controller = BookController()

    # 定义显示菜单函数
    def display_menu(self):
        print("按1选择增加图书")
        print("按2选择查询图书")
        print("按3选择删除图书")
        print("按4选择修改图书")

    # 定义选择菜单
    def select_menu(self):
        number = input("请输入选项")
        if number == "1":
            self.controller.add_book(self.input_book())
        elif number == "2":
            self.display_book()
        elif number == "3":
            self.controller.delete_book()
        elif number == "4":
            self.controller.modify_book()
        else:
            return True

    # 定义查询函数
    def display_book(self):
        for i in range(len(self.controller.list_book)):
            self.controller.list_book[i].display()

    def input_book(self):
        new_book = BookModel(input("请输入书本名称"), int(input("请输入书本单价")), input("请输入出版社名称"))
        return new_book

    def ensure_book(self):
        name = input("请输入书本名称")
        return name


class BookController:
    """
    控制器：负责处理业务逻辑，比如储存、计算
    """

    def __init__(self):
        self.list_book = []

    # 定义增加函数
    def add_book(self, model):
        self.list_book.append(model)

    # 定义删除函数
    def delete_book(self):
        del_name = input("请输入要删除的书本名称")
        for i in range(len(self.list_book)):
            if del_name == self.list_book[i].name:
                del self.list_book[i]
                break

    # 定义修改干数
    def modify_book(self):
        modi_name = input("请输入要修改的书本名称")
        for i in range(len(self.list_book)):
            if modi_name == self.list_book[i].name:
                new_book = BookModel(input("请输入书本名称"), int(input("请输入书本单价")), input("请输入出版社名称"))
                self.list_book[i] = new_book
                break


# ——————————程序入口——————————————
view = BookView()
while True:
    view.display_menu()
    view.select_menu()
