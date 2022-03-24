def print_log(function):

    def wrapper(*args):
        print("some_func была исполнена")
        result = function(*args)
        return result
    return wrapper


@print_log
def some_func(x, y):
    return x*y


print(some_func(4, 6))
