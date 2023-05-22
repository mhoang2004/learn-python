from time import time
from functools import wraps


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Time is: {end_time - start_time}")
        return result
    return wrapper

# sum_nums = speed_test(sum_nums)


@speed_test
def sum_nums():
    return sum((i for i in range(1000000)))


print(sum_nums())
