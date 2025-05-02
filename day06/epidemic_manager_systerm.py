list_epidemic = []
while True:
    print("按1录入地区")
    print("按2显示疫情情况")
    print("按3删除疫情信息")
    print("按4更新疫情信息")
    number = input("请输入选项：")
    # 录入
    if number == "1":
        dict_epidemic = {
            "region": input("请输入地区"),
            "add": int(input("请输入新增人数")),
            "now": int(input("请输入现有人数"))
        }
        list_epidemic.append(dict_epidemic)
    elif number == "2":
        for item in list_epidemic:
            print("%s地区新增%s人，目前共有%s名患者" % (item["region"], item["add"], item["now"]))
    elif number == "3":
        del_region = input("请输入您要删除的地区名称")
        for i in range(len(list_epidemic)):
            if list_epidemic[i]["region"] == del_region:
                del list_epidemic[i]
                break
    elif number == "4":
        change_region = input("请输入您需要修改地区的名称")
        for i in range(len(list_epidemic)):
            if list_epidemic[i]["region"] == change_region:
                list_epidemic[i]["region"] = input("请输入需要更改的地区名称")
                list_epidemic[i]["add"] = int(input("请输入需要更改的新增人数"))
                list_epidemic[i]["now"] = int(input("请输入需要更改的现有人数"))
                break
