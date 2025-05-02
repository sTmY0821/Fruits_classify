dic_taiwan = {"新增": 16, "现有": 1339, "累计": 16931, "治愈": 13742, "死亡": 850}
dic_shanxi = {"新增": 182, "现有": 859, "累计": 1573, "治愈": 711, "死亡": 3}
dic_zhejiang = {"新增": 2, "现有": 505, "累计": 2008, "治愈": 1502, "死亡": 1}
dic_guangxi = {"新增": 6, "现有": 256, "累计": 599, "治愈": 341, "死亡": 2}
dic_xianggang = {"新增": 9, "现有": 196, "累计": 12598, "治愈": 12189, "死亡": 213}
dic_shanghai = {"新增": 8, "现有": 153, "累计": 3056, "治愈": 2896, "死亡": 7}

dic_taiwan["新增"] = 8
dic_taiwan["医生"] = 8
del dic_taiwan["死亡"]
print(dic_taiwan)

for key in dic_taiwan:
    print(key)
for value in dic_shanxi.values():
    print(value)
for key, value in dic_zhejiang.items():
    print(key,value)
for key,value in dic_taiwan.items():
    if value ==2339:
        print(key)