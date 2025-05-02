from bll import EpidemicController
from dtl import EpidemicModel


class EpidemicView:
    def __init__(self):
        self.controller = EpidemicController()

    def display_menu(self):
        print("""
        1.添加疫情信息
        2.删除疫情信息
        3.修改疫情信息
        4.展示疫情信息
        5.退出系统
        """)

    def select_menu(self):
        number = int(input("请输入功能序号："))
        if number == 1:
            self.controller.add_epidemic(self.update_epidemic())
        elif number == 2:
            self.delete_epidemic()
        elif number == 3:
            self.modify_epidemic()
        elif number == 4:
            self.display_epidemic()
        elif number == 5:
            exit()
        else:
            print("输入有误，请重新输入")

    def update_epidemic(self):
        update_data = EpidemicModel(
            area=input("请输入地区："),
            current_people=int(input("请输入现有人数：")),
            increase_people=self.get_number("请输入新增人数：")
        )
        return update_data

    def delete_epidemic(self):
        area_name = input("请输入地区名称：")
        if self.controller.delete_epidemic(area_name):
            print("删除成功")
        else:
            print("删除失败")

    def modify_epidemic(self):
        area_name = input("请输入地区名称：")
        model = self.update_epidemic()
        if self.controller.modify_epidemic(area_name, model):
            print("修改成功")
        else:
            print("修改失败")

    def display_epidemic(self):
        for i in self.controller.epidemic_list:
            print(i)

    @staticmethod
    def get_number(message):
        while True:
            try:
                number = input(message)
                if number.isdigit():
                    return int(number)
            except:
                print("请输入数字")