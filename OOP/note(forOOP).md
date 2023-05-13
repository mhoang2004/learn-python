# What is OOP

- OOP just about using code to represent and recreate things exist in the world
- OOP attempts to model some process or thing as a "class" and "object"

- if define a class only holds methods and no data, won't need an `__init__` method

- the self keyword refers to specifics instance of the class we are working with

- why `_name`, `__name`, `__name__`

* `_name`: it is a private variable or private property (private in OOP)

* `__name`: python will do something with those variables (changes the name but not hiding)

* `__name__`: they are use for Python specific methods like init, we will define on our own

- Example

```python
class Person:
    def __init__(self):
        self.name = "Tony"
        self._greeting = "Hi!"
        self.__msg = "I like coding"
```

Method: - class attributes (define by dev)

# class method:

- some func doesn't care about the instances

# `__repr`

- representation
- define a representation of an instance

```python
def __repr__(self):
    return f"My name is {self.name}, I come from {self.city}"

user1 = User("tom", "texas")
print(user1) #My name is tom, I come from texas

```

# Method resolution order (MRO)

- when ever create a class, python will automatically sets a method resolution order (MRO)
  for the class
- we can see the oder or a class (what method class will priority)

# Polymorphism introduction

- an object can have many form
- the same class method works in a similar way for different class

  ```python
      Cat.speak() #meow
      Dog.speak() #woof
      Human.speak() #yo

  ```

  => print the sound of animal, but each class not the same sound

- the same operation works for different kinds of objects

  ```python
      sample_list = [1, 2, 3]
      sample_string = "awesome"
      len(sample_list)
      len(sample_string)
  ```

  => return the length of thing but in some form
