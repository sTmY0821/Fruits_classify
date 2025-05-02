import random

terget = random.randint(1, 100)
number = 0
while number != terget:
    for count in range(5):
        number = int(input("请输入一个数字"))
        if number > terget:
            print("大了")
        elif number < terget:
            print("小了")
        else:
            print("Bingo!!")
            break
