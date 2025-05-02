import copy
class MyClass:
    def __init__(self):
        self.data01 = 10
        self.data02 = [20]

m1 = MyClass()
m2 = m1
m3 = copy.copy(m1)
m4 = copy.deepcopy(m1)
m1.data01 = 100
m2.data02[0] = 200
print(m2.__dict__)
print(m3.__dict__)
print(m4.__dict__)