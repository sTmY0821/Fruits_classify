from day14.library_manager_system_v7.bll import LibraryController
from day14.library_manager_system_v7.dtl import LibraryModel


class LibraryView:
    def __init__(self):
        self.controller = LibraryController()

    def display_menu(self):
        print("按1键录入图书")
        print("按2键显示图书")
        print("按3键删除图书")
        print("按4键修改图书")

    def select_menu(self):
        try:
            number = input("请输入操作编号：")
            if number not in ["1", "2", "3", "4"]:
                raise Exception
            if number == "1":
                self.controller.add_book(self.input_book())
            elif number == "2":
                self.display_library()
            elif number == "3":
                self.delete_library()
            elif number == "4":
                self.modify_library()
        except Exception:
            print("输入有误，请重新输入")

    def input_book(self):
        model = LibraryModel(
            input("请输入图书名称："),
            input("请输入出版社："),
            self.input_float("请输入图书价格：")
        )
        return model

    @staticmethod
    def input_float(message):
        while True:
            try:
                number = float(input(message))
                return number
            except Exception:
                print("输入有误，请重新输入")

    def display_library(self):
        for book in self.controller.library_list:
            print(book)

    def delete_library(self):
        name = input("请输入要删除图书的名称：")
        if self.controller.delete_book(name):
            print("删除成功")
        else:
            print("删除失败")

    def modify_library(self):
        name = input("请输入要修改图书的名称：")
        model = self.input_book()
        if self.controller.modify_book(name, model):
            print("修改成功")
        else:
            print("修改失败")