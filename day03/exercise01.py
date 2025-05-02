while True:
    if input("Input") == "y":
        number = int(input("Enter a number: "))
        if number > 0:
            print("正数")
        elif number < 0:
            print("负数")
        elif number == 0:
            print("零")
    else:
        break
