list_range = [i for i in range(10,31) if i%3 ==0 or i %5 ==0]
print(list_range)
list_iterm = [j**2 for j in list_range]
print(list_iterm)
