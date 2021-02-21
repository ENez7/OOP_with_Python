
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

def main():
    a = int(input("A: "))
    b = int(input("B: "))
    print(addition(a, b))
    print(substraction(a, b))
    salute_person("Constantina Guess")

if __name__ == "__main__":
    main() 