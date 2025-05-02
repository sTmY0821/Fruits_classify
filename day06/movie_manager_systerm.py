"""
电影信息管理系统V1
    增加
    查询
    删除
    修改
"""
def modify_movie():
    global i
    change_movie = input("请输入您要修改的电影名称")
    for i in range(len(list_movie)):
        if list_movie[i]["name"] == change_movie:
            list_movie[i]["name"] = input("请输入您要修改的电影名字")
            list_movie[i]["type"] = input("请输入您要修改的电影类型")
            list_movie[i]["actor"] = input("请输入您要修改的电影演员")
            list_movie[i]["index"] = int(input("请输入您要修改的电影热搜指数"))
            break


def input_movie():
    dic_row = {
        "name": input("请输入电影名:"),
        "type": input("请输入电影类型:"),
        "actor": input("请输入电影主演名:"),
        "index": int(input("请输入电影热搜指数:"))
    }
    list_movie.append(dic_row)


def display_movie():
    for iterm in list_movie:
        print("%s电影的类型是%s，主演是%s，热搜指数为%s"% (iterm["name"], iterm["type"], iterm["actor"],iterm["index"]))


def delete_movie():
    del_movie = input("请输入您要删除的电影名称")
    for i in range(len(list_movie)):
        if list_movie[i]["name"] == del_movie:
            list_movie.remove(list_movie[i])
            break


def display_menu():
    print("按1键录入电影")
    print("按2键显示电影")
    print("按3键删除电影")
    print("按4键修改电影")


def select_menu():
    number = input("请输入选项:")
    if number == "1":
        # 3.录入电影
        input_movie()
    elif number == "2":
        # 4.显示电影
        display_movie()
    elif number == "3":
        # 5.删除电影
        delete_movie()
    elif number == "4":
        # 6.修改电影
        modify_movie()


list_movie = []
while True:
    # 1.显示菜单
    display_menu()
    # 2.选择菜单
    select_menu()
