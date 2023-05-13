class User:
    active_user = 0

    @classmethod  # when define a class method, start with this
    def get_active_user(cls):  # cls actually is a class
        return f"There are {cls.active_user} active user!"

    def __init__(self, name, city, age):
        self.name = name
        self.city = city
        self.age = age
        User.active_user += 1

    def __repr__(self):
        return f"My name is {self.name}, I come from {self.city}"

    def from_string(data_string):
        name, city, age = data_string.split(",")
        # string.split(separator, maxsplit) / ",", how many splits to do ======> [name, city, age]
        return User(name, city, int(age))


user1 = User.from_string("John,Texas,12")
user2 = User.from_string("Tom,California,18")

print(user1, user2)


# class Car:
#     wheels = 4

#     @classmethod
#     def change_wheels(cls, number_of_wheels):
#         cls.wheels = number_of_wheels


# car1 = Car()
# car2 = Car()

# print(car1.wheels)  # 4
# print(car2.wheels)  # 4

# Car.change_wheels(3)

# print(car1.wheels)  # 3
# print(car2.wheels)  # 3

# car1.change_wheels = 2
# print(car1.wheels)  # 3
