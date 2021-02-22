import random

def binary_search(data, begin, end, obj):
    # data = sorted(data)
    # As long as python doesn't pass by reference, we need to
    # return and reassign to keep the changes made into the function
    # more details: https://realpython.com/python-pass-by-reference/
    if begin >= end:
        return False

    half = (begin + end) // 2 
    # 2 SLASHES MEAN INT DIVISION

    # Debuggin reasons, can ignore it
    #print('----------------')
    #print(f'BEGIN: {begin}')
    #print(f'END: {end}')
    #print(f'HALF: {half}')
    #print(f'OBJ: {obj}')
    #print('----------------')
    
    if data[half] == obj:
        return True
    elif data[half] < obj:
        return binary_search(data, half+1, end, obj)
    else:
        return binary_search(data, begin, half-1, obj)
    
if __name__ == '__main__':
    size = int(input('Size: '))
    obj = int(input('Search for: '))
    
    data = sorted([random.randint(0, 10) for i in range(size)])
    #data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] Modify to try your custom data
    found = binary_search(data, 0, len(data), obj)
    
    print(data)
    print(f'\nElement {obj} {"is in" if found else "is not in"} data list')