# 第一题
father_height = int(input("Enter Father Height: "))
mother_height = int(input("Enter Mother Height: "))
forecasting_child_height = (father_height + mother_height) * 0.54
print("孩子的身高预计为"+str(int(forecasting_child_height)))
# 第二题
print("华氏度为" + str(int((int(input("请输入摄氏度")) - 32) / 1.8)))
# 第三题
salary = int(input("Enter Salary: "))
print("个人社保缴纳费用为" + str(salary * 0.08 + salary * 0.02 + 3 + salary * 0.002 + salary * 0.12))
# 第四题
month = int(input("Enter Month: "))
if month in (1, 3, 5, 7, 8, 10, 12):
    print("这个月有" + "31" + "天")
elif month == 2:
    print("这个月有" + "28" + "天")
elif month in (4, 6, 9, 11):
    print("这个月有" + "31" + "天")
else:
    print("请输入正确的月份")
