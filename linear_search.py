import random

def linear_search(data, objective):
    match = False
    
    for element in data:
        if element == objective:
            match = True
            break
    
    return match

if __name__ == '__main__':
    
    list_size = int(input('Size: '))
    objective = int(input("Search for: "))
    data = [random.randint(0, 5) for i in range(list_size)]
    
    found = linear_search(data, objective)
    print(data)
    print(f'Element {objective} {"is in" if found else "is not in"} data list')