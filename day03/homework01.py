# 2.1 猜对了

# 2.2 大于3

# 3.1
age = int(input("Enter your age: "))
if age in range(0, 7):
    print("童年")
elif age in range(7, 18):
    print("少年")
elif age in range(18, 41):
    print("青年")
elif age in range(41, 66):
    print("中年")
elif age > 65:
    print("老年")

# 3.2
cost = 0
if_vip = input("请输入账户类型（Y/N）来判定你是否为VIP客户")
amount_spent = int(input("请输入消费金额"))
if if_vip == "Y":
    if amount_spent <= 500:
        cost = amount_spent * 0.85
    else:
        cost = amount_spent * 0.8
elif if_vip == "N":
    if amount_spent >= 800:
        cost = amount_spent * 0.9
    else:
        cost = amount_spent
print(cost)
