class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()  # repr of class dict

    def __missing__(self, key):  # what will print if the key is missing
        return f"You want {key}? Well, it does not here!"

    def __setitem__(self, key, value):
        print("Why you always have to change things?")
        print("Well, alright, do it...")
        super().__setitem__(key, value)


test = dict({'first': 'Jerry', 'animal': 'mouse'})
data = GrumpyDict({'first': 'Tom', 'animal': 'cat'})

print(data)
print(data["name"])
data['animal'] = 'animation cat'
print(data['animal'])
