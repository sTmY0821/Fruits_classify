list_book = []


def display_menu():
    print("按1输入书本信息")
    print("按2显示书本信息")
    print("按3删除书本信息")
    print("按4修改书本信息")


def select_menu():
    number = input("请输入数字选择操作")
    if number == "1":
        input_book()
    if number == "2":
        display_book()
    if number == "3":
        delete_book()
    if number == "4":
        modify_book()


def input_book():
    dict_input_book = {
        "name": input("请输入书本的名称"),
        "price": float(input("请输入书本的单价")),
        "publisher": input("请输入出版社名称")
    }
    list_book.append(dict_input_book)


def display_book():
    for iterm in list_book:
        print("名为%s书本的单价为%s元，出版社是%s" % (iterm["name"], iterm["price"], iterm["publisher"]))


def delete_book():
    del_name_book = input("请输入您要删除的书本名字")
    for iterm in list_book:
        if del_name_book == iterm["name"]:
            list_book.remove(iterm)
            break


def modify_book():
    modi_name_book = input("请输入您要修改的书本名字")
    for i in range(len(list_book)):
        if modi_name_book == list_book[i]["name"]:
            list_book[i] = {
                "name": input("请输入修改后书本的名称"),
                "price": float(input("请输入修改的书本单价")),
                "publisher": input("请输入修改的出版社名称")
            }
            break


while True:
    display_menu()
    select_menu()
