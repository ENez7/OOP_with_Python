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
        left_side_iterator = 0
        right_side_iterator = 0
        # Iterator for main list
        main_list_iterator = 0
        
        while left_side_iterator < len(left_side) and right_side_iterator < len(rigth_side):
            if left_side[left_side_iterator] < rigth_side[right_side_iterator]:
                data[main_list_iterator] = left_side[left_side_iterator]
                left_side_iterator += 1
            else:
                data[main_list_iterator] = rigth_side[right_side_iterator]
                right_side_iterator += 1
            main_list_iterator += 1
        
        # These while's below are for the remaining data in the sub-arrays
        while left_side_iterator < len(left_side):
            data[main_list_iterator] = left_side[left_side_iterator]
            left_side_iterator += 1
            main_list_iterator += 1
        
        while right_side_iterator < len(rigth_side):
            data[main_list_iterator] = rigth_side[right_side_iterator]
            right_side_iterator += 1
            main_list_iterator += 1
    
    return data
        
        
if __name__ == '__main__':
    size = int(input("Size: "))
    
    data_list = [random.randint(0, 100) for i in range(size)]
    print(data_list)
    print('--' * 20) # -- <-this 20 times
    data_list = merge_sort(data_list)
    print(data_list)