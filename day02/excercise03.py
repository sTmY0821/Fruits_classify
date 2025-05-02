number = int(input("Enter a number: "))
sum = 0
while number >= 1:
    sum += number % 10
    number //= 10
print(sum)
