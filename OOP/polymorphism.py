# the same class method works on in a similar way for different way for different classes

class Animal():
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")


class Dog():
    def speak(self):
        return "woof"


class Cat():
    def speak(self):
        return "meow"

# the same operation works for different kinds of objects


class Human:
    def __init__(self, last, first, age):
        self.last = last
        self.first = first
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first=self.first, last=other.last, age=0)
        return "You can't add that!"

    def __mul__(self, other):
        if isinstance(other, int):
            return [self for i in range(other)]
        return "Can't multiply"


j = Human("Jane", "Bill", 19)
k = Human("Kevin", "Jones", 21)
print((k+j) * 2)  # when write + (python will call __add__)
