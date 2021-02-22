import random

def merge_sort(data):
    if len(data) > 1:
        half = len(data) // 2
        left_side = data[:half] # Pick up data from 0 to half index
        rigth_side = data[half:] # Pick up data from half until last index

        # Recursive calls until len(data) is equal to 1
        merge_sort(left_side)
        merge_sort(rigth_side)
        
        # Iterators for sub-lists
        i = 0
        j = 0
        # Iterator for main list
        k = 0
        
        while i < len(left_side) and j < len(rigth_side):
            if left_side[i] < rigth_side[j]:
                data[k] = left_side[i]
                i += 1
            else:
                data[k] = rigth_side[j]
                j += 1
            k += 1
        
        # These while's below are for the remaining data in the sub-arrays
        while i < len(left_side):
            data[k] = left_side[i]
            i += 1
            k += 1
        
        while j < len(rigth_side):
            data[k] = rigth_side[j]
            j += 1
            k += 1
    
    return data
        
        
if __name__ == '__main__':
    size = int(input("Size: "))
    
    data_list = [random.randint(0, 100) for i in range(size)]
    print(data_list)
    print('--' * 20) # -- <-this 20 times
    data_list = merge_sort(data_list)
    print(data_list)