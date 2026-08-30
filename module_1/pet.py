class Pet:
    def __init__(self, name, species, age):
        self.age = age
        self.name = name
        self.species = species

    def setName(self, newName):
        self.setName = newName

    def getName(self):
        return self.name

    def setAge(self, newAge):
        self.setAge = newAge

    def getAge(self):
        return self.age

    def setSpecies(self, newSpecies):
        self.setSpecies = newSpecies

    def getSpecies(self):
        return self.species

    def describe(self):
        print(f'{self.name} is a {self.age}-year-old {self.species}')

    def birthday(self):
        self.age = self.getAge() + 1
        print(f'Happy birthday {self.name}! You are now {self.age} years old.')



def main():
    p1 = Pet("Luna", "Dog", 3)

    p2 = Pet("Nova", "Reptile", 4)
    
    p3 = Pet("Shadow", "Argonian", 77)

    p1.describe()
    p2.describe()
    p3.describe()
    p1.birthday()
    
main()

