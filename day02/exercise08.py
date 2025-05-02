mental_age = int(input("Enter your mental age: "))
chronological_age = int(input("Enter your chronological age:"))
iq=int(int(mental_age)/int(chronological_age)*100)
if iq>=140:
    print("Genius")
elif 139>=iq>=120:
    print("Excellent")
elif 119>=iq>=110:
    print("Clever")
elif 109>=iq>=90:
    print("Normal")
elif 89>=iq>=80:
    print("Obtuse")
elif iq<80:
    print("Retarded mind")