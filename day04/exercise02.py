list_area = ["台湾","陕西","浙江"]
list_add = [16,182,2]
list_now = [2339,859,505]

print(max(list_add))
print(min(list_now))
print(sum(list_now))
print(859 in list_now)

list_area.append("广西")
list_now.append(256)
list_add.append(6)
list_epidemic_area=[]
for num in range (5):
    list_epidemic_area.append(input("请输入疫情地区名称"))
print(list_epidemic_area)