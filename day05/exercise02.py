# days = (31,29,31,30,31,30,31,31,30,31,30,31)
# month = int(input("请输入月份"))
# day = int(input("请输入日期"))
# total_days = 0
# for i in range(month-1):
#     total_days += days[month-1]
# total_days +=day
#使用切片
days = (31,29,31,30,31,30,31,31,30,31,30,31)
month = int(input("请输入月份"))
day = int(input("请输入日期"))
total_days = sum(days[:month-1])+day
print("您输入的日期是这一天的第"+str(total_days)+"天")

