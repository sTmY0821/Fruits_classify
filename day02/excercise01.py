weight = float(input("Enter your weight : "))
weight_in_jin=weight//16
weight_in_liang=weight%16
print(str(int(weight_in_jin))+"斤"+str(int(weight_in_liang))+"两")