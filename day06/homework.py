list_book = []
while True:
    print("按1增加书本信息")
    print("按2显示书本信息")
    print("按3删除书本信息")
    print("按4修改书本信息")
    number = input("请输入选项进行操作")
    if number == "1":
        add_book = {
            "name": input("请输入增加的书本名字"),
            "price": float(input("请输入书本的单价")),
            "publisher": input("请输入出版社名称")
        }
        list_book.append(add_book)
    if number == "2":
        for book in list_book:
            print("%s这本书的单价为%s，出版社是%s" % (book["name"], book["price"], book["publisher"]))
    if number == "3":
        del_book = input("请输入您要删除书本的名字")
        for i in range(len(list_book)):
            if list_book[i]["name"] == del_book:
                list_book.remove(list_book[i])
                break
    if number == "4":
        change_book = input("请输入您要修改书本的名字")
        for i in range(len(list_book)):
            if list_book[i]["name"] == change_book:
                list_book[i]["name"] = input("您要修改的书本名字是")
                list_book[i]["price"] = float(input("请输入您要修改的单价"))
                list_book[i]["publisher"] = input("请输入您要修改的出版社名称")
                break
