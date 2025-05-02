menu = []
def display_menu():
    print("按1选择增加餐厅")
    print("按2选择查询餐厅")
    print("按3选择删除餐厅")
    print("按4选择修改餐厅")

def select_menu(number):
    if number == "1":
        add_restrant()
    elif number == "2":
        display_restrant()
    elif number == "3":
        delete_restrant()
    elif number == "4":
        modify_restrant()


def add_restrant():
    dict_restrant = {
        "name":input("请输入餐厅名"),
        "city":input("请输入城市名"),
        "per_consumption":int(input("请输入人均消费"))
    }
    menu.append(dict_restrant)

def display_restrant():
    for i in range(len(menu)):
        print("%s餐厅位于%s，人均消费%s元"%(menu[i]["name"],menu[i]["city"],menu[i]["per_consumption"]))

def delete_restrant():
    del_restrant = input("请输入需要删除的餐厅名字")
    for i in range(len(menu)):
        if del_restrant == menu[i]["name"]:
            del menu[i]


def modify_restrant():
    modi_restrant = input("请输入需要修改的餐厅名字")
    for i in range(len(menu)):
        if modi_restrant == menu[i]["name"]:
            menu[i]={
                "name":input("请输入餐厅名"),
                "city":input("请输入城市名"),
                "per_consumption":int(input("请输入人均消费"))
            }



#-----------程序入口------------------
while True:
    display_menu()
    select_menu(input("请输入数字选择操作"))