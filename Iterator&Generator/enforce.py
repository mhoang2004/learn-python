def enforce(*type):
    def decorator(f):
        def new_func(*args, **kwargs):
            new_args = []
            for (a, t) in zip(args, type):
                new_args.append(t(a))
            print(kwargs)
            print(args)
            return f(*new_args, **kwargs)
        return new_func
    return decorator


@enforce(str, int)
def repeat_msg(msg, times, status="successfully"):
    for time in range(times):
        print(msg)
    print(status)


@enforce(float, float)
def divide(a, b):
    return a/b


repeat_msg("hello", "7", status="completed")
# print(divide("1", "7"))
