# 创建疫情类型
class EpidemicCity:
    def __init__(self, region, add_population, now_population):
        self.region = region
        self.add_population = add_population
        self.now_population = now_population

    def display(self):
        print("%s区域目前新增人数%s人，当前人数为%s人" % (self.region, self.add_population, self.now_population))


# 定义显示菜单函数
def display_menu():
    print("按1选择增加疫情情况")
    print("按2选择查询疫情情况")
    print("按3选择删除疫情情况")
    print("按4选择修改疫情情况")


# 定义选择菜单
def select_menu(number):
    if number == "1":
        add_epidemic()
    elif number == "2":
        display_epidemic()
    elif number == "3":
        delete_epidemic()
    elif number == "4":
        modify_epidemic()
    else:
        return True


# 定义增加函数
def add_epidemic():
    add_epid = EpidemicCity(input("请输入地区名称"), int(input("请输入新增人数")), int(input("请输入目前人数")))
    list_epidemic.append(add_epid)


# 定义查询函数
def display_epidemic():
    for i in range(len(list_epidemic)):
        list_epidemic[i].display()


# 定义删除函数
def delete_epidemic():
    del_region = input("请输入要删除的地区名称")
    for i in range(len(list_epidemic)):
        if del_region == list_epidemic[i].region:
            del list_epidemic[i]
            break


# 定义修改干数
def modify_epidemic():
    modi_region = input("请输入要修改的地区名称")
    for i in range(len(list_epidemic)):
        if modi_region == list_epidemic[i].region:
            new_epidemic = EpidemicCity(input("请输入地区名称"), int(input("请输入新增人数")),
                                        int(input("请输入目前人数")))
            list_epidemic[i] = new_epidemic
            break


# ——————————程序入口——————————————
list_epidemic = []
while True:
    display_menu()
    select_menu(input("请输入数字选择您的需求"))
