class Collar:
    def __init__(self, name_string, size, is_tracked):
        self.name_string = name_string
        self.size = size
        self.is_tracked = is_tracked

class Pet:
    def __init__(self, name, species, collar):
        self.name = name
        self.species = species
        self.collar = collar

class Person:
    def __init__(self, name, pet):
        self.name = name
        self.pet = pet



collar1 = Collar("Chris's Collar", "Fitted", True)
pet = Pet("Chris", "Cat", collar1)
person = Person("Christian", pet)


print(person.name)
print(person.pet.name)
print(person.pet.collar.name_string)
print(person.pet.collar.size)
print(person.pet.collar.is_tracked)