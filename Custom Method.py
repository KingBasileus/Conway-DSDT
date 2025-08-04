class Dog:
    def __init__(self):
        self.speed = 0

    def bark(self):
        print("bark")
    
    def run(self):
        self.speed = 30
    
    
class Cat:
    def meow():
        print("meow")

class Parrot:
    def __init__(self):
        self.hp = 1

    def eat(self):
        self.hp += 1

dog = Dog()
parrot = Parrot()

dog.run()
print(dog.speed)

parrot.eat()
print(parrot.hp)