def insertion_sort(data_list):

    for index in range(1, len(data_list)):
        current_value = data_list[index]
        current_pos = index

        while current_pos > 0 and data_list[current_pos - 1] > current_value:
            data_list[current_pos] = data_list[current_pos - 1]
            current_pos -= 1

        data_list[current_pos] = current_value
    return data_list

if __name__ == '__main__':
    data = [2, 3 , 5, 7, 2 ,7, 9, 1, 0, -1]
    # Change this value or random generate them to test another cases
    
    data = insertion_sort(data)
    print(data)
    # Output: [-1, 0, 1, 2, 2, 3, 5, 7, 7, 9]