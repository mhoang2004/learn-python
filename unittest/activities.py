from random import choice

def eat(name, is_healthy):
    if not isinstance(is_healthy, bool):
        raise ValueError("is_healthy must be a boolean")
    ending = "YOLO"
    if is_healthy:
        ending = "my body is a temple"
    return f"I'm eating {name}, because " + ending 

def nap(num):
    if num < 2:
        return f"I'm feeling refreshed after my {num} hour nap"
    else:
        return f"Ugh I overslept. I did not mean to nap for {num} hours"
    
def is_funny(person):
    if person is "tim": return False
    return True

def laugh():
    laugh_tuple = ('haha', 'lol', 'tehehe')
    return choice(laugh_tuple)



