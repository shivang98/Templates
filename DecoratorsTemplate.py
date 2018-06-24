import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("I'm inside decorator")
        func()
        print("After function executes")
    return function_that_runs_func

@my_decorator
def my_function1():
    print("Hello World")

# my_function()

def decorator_with_arguments(num):
    def my_decorator(func):
        functools.wraps(func)
        def function_that_runs_func(*args, **kargs):
            print("I'm inside decorator")
            if num == 47:
                func(*args, **kargs)
            else:
                print("You are not allowed to use this section")
            print("After function executes")
        return function_that_runs_func
    return my_decorator

@decorator_with_arguments(47)
def my_function2(a, b):
    print(a + b)

# my_function2(10, 20)