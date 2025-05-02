#第一题
list_plant = ["水星","金星","火星","木星"]
list_plant.insert(2,"地球")
list_plant.append("金星")
list_plant.append("天王星")
list_plant.append("海王星")
print(list_plant[0]+list_plant[-1])
print(list_plant[:2])
list_plant.remove("海王星") #del list_plant[3]


#第二题
list_ensure =[]
for i in range(5):
    list_ensure.append(int(input("请输入5个省份的确诊人数")))
print(min(list_ensure))
print(max(list_ensure))
print(sum(list_ensure))
print(len(list_ensure))