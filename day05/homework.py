# 第一题
list_number01 = [4, 5, 6, 7, 8, 1, 9, 3]
list_number02 = [7, 5, 9, 7, 1]
list_even01 = [i for i in list_number01 if i % 2 == 0]
list_even02 = [j for j in list_number02 if j % 2 == 0]
print("列表一的偶数平均值为%.d" % (sum(list_even01) / len(list_even01)))
if len(list_even02) !=0:
    print("列表二的偶数平均值为%.d" % (sum(list_even02) / len(list_even02)))
else:
    print("列表二不包含偶数")

# 第二题
list_number = [4, 5, -6, 7, 8, 0, 9, -3, 0]
positive_num = 0
negative_num = 0
zero_num = 0
for i in list_number:
    if i > 0:
        positive_num += 1
    elif i < 0:
        negative_num += 1
    elif i == 0:
        zero_num += 1
print("正数有%s个，负数有%s个，零有%s个" % (positive_num, negative_num, zero_num))
