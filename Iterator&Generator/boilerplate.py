from functools import wraps


def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # logic goes in here...
        pass
    return wrapper

# What we are really doing?


def decorator():
    pass

# when we write


@decorator
def func(*args, **kwargs):
    pass


# we're really doing:
func = decorator(func)

# when we write


@decorator(name)
def func(*args, **kwargs):
    pass


# we're really doing:
func = decorator(name)(func)
