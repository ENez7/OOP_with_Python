# reference: https://realpython.com/primer-on-python-decorators/

import functools

# Decorator functions with args must always return a value
# in order to get the results of the decorated function
# that receives the actual parameters
def decorator_function(func_as_param):
    def internal_func(*args, **kwargs):
        print("Internal function")
        result = func_as_param(*args, **kwargs)
        print("End of internal function")
        return result
    return internal_func

@decorator_function
def addition(a: int, b: int):
    return a + b

@decorator_function
def substraction(a: int, b: int):
    return a - b

def greetings(func_as_param):
    def internal_func(*args, **kwargs):
        func_as_param(*args, **kwargs)
        print("How are you today?")
    return internal_func

@greetings
def salute_person(name):
    print(f'Hello {name}')

# Decorators with args
def repeat(num_times):
    def dec(func):
        def wrapper(*a, **kw):
            for i in range(num_times):
                func(*a, **kw)
        return wrapper
    return dec

@repeat(num_times = 0)
def greet(name):
    print(f'Hello {name}')

# Caching return values
def cache(func):
    @functools.wraps(func)
    def wrapper_cache(*a, **kw):
        cache_key = a + tuple(kw.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*a, **kw)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache

@cache
def fibonnaci(num):
    if num < 2:
        return num
    return fibonnaci(num - 1) + fibonnaci(num - 2)

# NOTE: LRU cache is available as @functools.lru_cache
# you should use this instead of your own cache decorator
# @functools.lru_cache(maxsize=4)
# def fibo(num):
#     if num < 2:
#         return num
#     return fibo(num - 1) + fibo(num - 2)


# This is important 'cause you use decorators to implement
# JSON validating functions when working with, for example, 
# Flask framework
# As example:
# @app.route('/grade', methods=['POST'])
# def update_grade():
#   body

def main():
    a = int(input("A: "))
    b = int(input("B: "))
    print(addition(a, b))
    print(substraction(a, b))
    salute_person("Constantina Guess")
    print('--------------------------')
    greet('Enrique')
    print('--------------------------')
    print('--------------------------')
    print(fibonnaci(10))
    print(fibonnaci(7))
    print(fibonnaci(0))

if __name__ == "__main__":
    main() 