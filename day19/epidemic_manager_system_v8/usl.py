from bll import EpidemicController
from dtl import EpidemicModel


class EpidemicView:
    def __init__(self):
        self.controller = EpidemicController()

    def display_menu(self):
        print("1.录入疫情")
        print("2.显示疫情")
        print("3.删除疫情")
        print("4.修改疫情")

    def select_menu(self):
        option = input("请输入选项：")
        if option == "1":
            self.controller.add_epidemic(self.input_epidemic())
        elif option == "2":
            self.display_epidemic()
        elif option == "3":
            self.delete_epidemic()
        elif option == "4":
            self.modify_epidemic()

    def input_epidemic(self):
        input_model = EpidemicModel(
            input("请输入疫情名称："),
            EpidemicView.input_int("请输入当前人数："),
            EpidemicView.input_int("请输入新增人数：")
        )
        return input_model

    def display_epidemic(self):
        for item in self.controller.epidemic_list:
            print(item)

    def delete_epidemic(self):
        del_region = input("请输入要删除的地区名称")
        if self.controller.delete_epidemic(del_region):
            print("删除成功")
        else:
            print("删除失败")

    def modify_epidemic(self):
        modify_region = input("请输入要修改的地区名称")
        if self.controller.modify_epidemic(modify_region, self.input_epidemic()):
            print("修改成功")
        else:
            print("修改失败")
    @staticmethod
    def input_int(message):
        while True:
            try:
                return int(input(message))
            except:
                print("输入有误")


