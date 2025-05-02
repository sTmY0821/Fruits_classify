"""
重写
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return "我叫%s,今年%s岁"%(self.name,self.age)


p = Person("张三", 20)
print(p)

list_person = [
    Person
    ("张三", 20),
    Person("李四", 30),
    Person("王五", 40)
]

print(Person("张三", 20)in list_person)
list_person.remove(Person("张三", 20))
print(Person("张三", 20)in list_person)