confirmed_cases_num=input("请输入确诊人数：")
cured_num=input("请输入治愈人数：")
cured_rate=float(cured_num)/float(confirmed_cases_num)
print(f'治愈比例为:{cured_rate=}%') 