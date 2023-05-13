class User:
    def __init__(self, first, last, age):  # self is not a parameter
        self.first = first  # the first argument will be first
        self.last = last    # self.last ~ User.last
        self.age = age
        self.num = 10


class Person:
    def __init__(self):
        self.name = "Tony"
        self._greeting = "Hi!"
        self.__msg = "I like coding"


# when declare a class it will be call __init__ function
user1 = Person()
print(dir(user1))
print(user1.name, user1._Person__msg, user1._greeting)
