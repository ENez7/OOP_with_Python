
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

def main():
    a = int(input("A: "))
    b = int(input("B: "))
    print(addition(a, b))
    print(substraction(a, b))

if __name__ == "__main__":
    main() 