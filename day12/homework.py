"""
1.疫情信息管理系统
创建疫情模型：
变量：地区、现有人数、新增人数
函数：重写__str__、__eq||

"""


class EpidemicModel:
    def __init__(self, area: str="", current_people: int=0, increase_people: int=0):
        self.area = area
        self.current_people = current_people
        self.increase_people = increase_people

    def __str__(self):
        # return f"地区：{self.area} 现有人数：{self.current_people} 新增人数：{self.increase_people}"
        return "%s地区目前疫情现有人数%s人，新增%s人" % (self.area, self.current_people, self.increase_people)

    def __eq__(self, other):
        return self.area == other.area


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
            increase_people=int(input("请输入新增人数："))
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


class EpidemicController:

    def __init__(self):
        self.epidemic_list = [] #type:list[EpidemicModel]

    def add_epidemic(self, model):
        self.epidemic_list.append(model)

    def delete_epidemic(self, area_name) -> bool:
        model = EpidemicModel(area_name)
        if model in self.epidemic_list:
            self.epidemic_list.remove(model)
        # for i in range(len(self.epidemic_list)):
        #     if self.epidemic_list[i].area == area_name:
        #         del self.epidemic_list[i]
            return True
        return False

    def modify_epidemic(self, area_name, model: EpidemicModel) -> bool:
        for i in range(len(self.epidemic_list)):
            if self.epidemic_list[i].area == area_name:
                self.epidemic_list[i] = model
                # self.epidemic_list[i].__dict__= model.__dict__
            return True
        return False


# ___________程序入口________________
epidemic = EpidemicView()
while True:
    epidemic.display_menu()
    epidemic.select_menu()
