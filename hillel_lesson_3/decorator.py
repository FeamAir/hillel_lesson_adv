from functools import wraps

def print_log(function):
    
    @wraps(function)
    def wrapper(*args):
        print(function.__doc__)
        result = function(*args)
        return result
    return wrapper


@print_log
def some_func(x, y):
    """some_func - this function 
    perfoms multiplication of numbers"""
    return x*y


print(some_func(4, 6))
