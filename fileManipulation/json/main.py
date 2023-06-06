import json

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
c = Cat("Charles", "Tabby")
d = Cat("Red", "Small")
    
# j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
# j = json.dumps(c.__dict__)

f = [c.__dict__, d.__dict__]

# turn to <str> and save to file
with open("cat.json", "w") as file:
    frozen = json.dumps(f)
    file.write(frozen)

# turn to dict again and use normal
with open("cat.json") as file:
    content = file.read()
    unfrozen = json.loads(content)
    print(unfrozen[1])


"""
JSON like CSV
Javasrcipt object notation

[

{
    "text": ,
    "author": ..,
    "author information": ...,
    "tag": ...,
},

]

"""