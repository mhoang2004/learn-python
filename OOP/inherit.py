class Animal:
    cool = True

    def __init__(self, age, first, last):
        self._age = max(0, age)
        self.first = first
        self.last = last

    def make_sound(self, sound):
        print(sound)

    @property
    def age(self):  # cat1.age #2 (we can get like this)
        return self._age

    @age.setter  # cat1.age = 22 (we can modified like this)
    def set_age(self, new_age):
        self._age = max(0, new_age)

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, new_name):
        self.first, self.last = new_name.split(" ")


class Things:
    height = 0
    weight = 0

    def can_move(self):
        print("This thing could move>")


class Cat(Animal, Things):
    def __init__(self, age, breed, toy):
        super().__init__(age)  # super will return Animal, so we don't have to
        # self.age = age
        self.breed = breed
        self.toy = toy


cat1 = Cat(2, 'blue', 'tom')

# print(cat1.cool)
# print(cat1.height)

print(cat1.age)
cat1.set_age = 2.4
print(cat1.age)

cat1.full_name = "Jerry Brown"
print(cat1.full_name)
