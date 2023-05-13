class Pet:
    allowed = ['cat', 'dog', 'bird', 'fish', 'rat']

    def __init__(self, name, species):
        if species not in self.allowed:  # Pet.allowed
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species
        print(self)

    def set_species(self, species):
        if species not in self.allowed:  # Pet.allowed
            raise ValueError(f"You can't have a {species} pet!")
        self.species = species
# ==========================
# self will be change within an instance, this won't effect in the class attribute or any other class
# class Chicken:
#     eggs = 0
#     total_eggs = 0
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def lay_egg(self):
#         Chicken.total_eggs += 1
#         self.eggs += 1
#         return self.eggs

# c1 = Chicken(name="Alice", species="Partridge Silkie")
# Chicken.total_eggs # c1.total_eggs

# =========================


dog = Pet("blue", "dog")
# cat = Pet("blue", "cat")
dog.allowed = ['cat', 'dog', 'bird', 'fish', 'lion']

# print(cat.allowed)

print(dog.allowed)


dog.set_species('lion')
