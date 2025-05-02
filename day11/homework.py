#homework 01
class AnimalModel:
    def eat(self):
        print("Animal eat")

class DogModel(AnimalModel):
    def walk(self):
        print("Dog walk")

class BirdModel(AnimalModel):
    def fly(self):
        print("Bird fly")

animal = AnimalModel()
dog = DogModel()
bird = BirdModel()
dog.eat()

#homework 02
