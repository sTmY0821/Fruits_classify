
from day19.library_manager_system_v8.bll import LibraryController
from day19.library_manager_system_v8.dtl import LibraryModel


class LibraryView:
    def __init__(self):
        self.controller = LibraryController()

    def display_menu(self):
        print("1.添加图书")
        print("2.删除图书")
        print("3.修改图书")
        print("4.查询图书")

    def select_menu(self):
        number = input("请输入数字选择操作")
        if number == "1":
            self.controller.add_book(self.add_library())
        elif number == "2":
            self.delete_library()
        elif number == "3":
            self.modify_library()
        elif number == "4":
            self.display_library()
        else:
            print("输入有误，请重新输入")

    def add_library(self):
        model = LibraryModel(
            name = input("请输入书名"),
            publisher = input("请输入出版社"),
            price = LibraryView.input_float("请输入价格")
        )
        return model

    @staticmethod
    def input_float(message):
        while True:
            try:
                return float(input(message))
            except ValueError:
                print("%s输入错误，请重新输入"%(message))

    def delete_library(self):
        name = input("请输入书名")
        if self.controller.delete_book(name):
            print("删除成功")
        else:
            print("删除失败")

    def modify_library(self):
        name = input("请输入书名")
        if self.controller.modify_book(name,LibraryModel(
            name = input("请输入书名"),
            publisher = input("请输入出版社"),
            price = LibraryView.input_float("请输入价格")
        )):
            print("修改成功")
        else:
            print("修改失败")

    def display_library(self):
        for item in self.controller.library_dao.load():
            print(item)
