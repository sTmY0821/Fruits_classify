# 创建疫情类型
class Book:
    def __init__(self, name, price, publisher):
        self.name = name
        self.price = price
        self.publisher = publisher

    def display(self):
        print("%s书本的单价为%s，出版社是%s" % (self.name, self.price, self.publisher))


# 定义显示菜单函数
def display_menu():
    print("按1选择增加图书")
    print("按2选择查询图书")
    print("按3选择删除图书")
    print("按4选择修改图书")


# 定义选择菜单
def select_menu(number):
    if number == "1":
        add_book()
    elif number == "2":
        display_book()
    elif number == "3":
        delete_book()
    elif number == "4":
        modify_book()
    else:
        return True


# 定义增加函数
def add_book():
    add_epid = Book(input("请输入书本名称"), int(input("请输入书本单价")), input("请输入出版社名称"))
    list_book.append(add_epid)


# 定义查询函数
def display_book():
    for i in range(len(list_book)):
        list_book[i].display()


# 定义删除函数
def delete_book():
    del_name = input("请输入要删除的书本名称")
    for i in range(len(list_book)):
        if del_name == list_book[i].name:
            del list_book[i]
            break


# 定义修改干数
def modify_book():
    modi_name = input("请输入要修改的书本名称")
    for i in range(len(list_book)):
        if modi_name == list_book[i].name:
            new_book = Book(input("请输入书本名称"), int(input("请输入书本单价")), input("请输入出版社名称"))
            list_book[i] = new_book
            break


# ——————————程序入口——————————————
list_book = []
while True:
    display_menu()
    select_menu(input("请输入数字选择您的需求"))
