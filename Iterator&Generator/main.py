from functools import wraps


def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)


def square(x):
    print(x*x)

# it do not need an array with 4 million beat


def current_beat():
    nums = (1, 2, 3, 4)
    i = 0
    while True:
        if i > len(nums):
            i = 0
        yield nums[i]
        i += 1


def fib_gen(max):
    x, y = 0, 1
    count = 0
    while count < max:
        x, y = y, x + y
        yield y  # it will reduce memory, if not we will need a list to store massive
        # of number (may be 1 million, 4 million or 1 billion), but it wil slower
        count += 1


def be_polite(fn):
    @wraps(fn)  # you pass fn in here and call be_polite
    # be_polite return wrapper
    # so doc and name will be the func you called (wrapper)
    # to prevent it we use wraps
    def wrapper():
        """I am a wrapper func"""
        print(f"you are about to call: {fn.__name__}")
        print(f"here's the documentation: {fn.__doc__}")
        print("What a pleasure to meet you!!")
        fn()
        print("Have a great day!!")
    return wrapper


def greet():
    print("My name is Hog!!")


@be_polite  # <=> rage = be_polite(rage)
def rage():
    """ print something rage """
    print("I hate you")


rage()
print(rage.__doc__)
print(rage.__name__)


wrapper_greet = be_polite(greet)

# if we @polite_rage we don't have to:
# rage = be_polite(rage)


# my_for([1, 2, 3, 4], square)
