from functools import wraps


def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed! Sorry")
        return fn(*args, **kwargs)
    return wrapper


def ensure_no_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if args:
            raise ValueError("No args allowed! Sorry")
        return fn(*args, **kwargs)
    return wrapper


@ensure_no_kwargs
def greet(name):
    print(f"hi there {name}")


@ensure_no_args
def rage(name, msg):
    print(f"{name} {msg}")


greet("Tony")
rage(name="Tony", msg="Hate")
