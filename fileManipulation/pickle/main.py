import pickle

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"This animal says {sound}")

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species = 'Cat')
        self.breed = breed
        self.toy = toy
    
    def play(self):
        return f"{self.name} plays with {self.toy}"

# blue = Cat("Blue", "Scottish Fold", "String")

# with open("pets.pickle", "wb") as file:
#     pickle.dump(blue, file) #`dump` take a tuple (blue, green, red, ...) 

with open("pets.pickle", "rb") as file:
    zombile_blue = pickle.load(file)
    print(zombile_blue)
    print(zombile_blue.play())

"""
Even we comment out the blue and `dump` it still know the blue
It store by binary

"""

