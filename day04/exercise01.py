sum_value=0
for number in range(10,61):
    if number % 10 == 3 or number % 10 ==5 or number % 10 ==8:
        continue
    sum_value += number
print(sum_value)