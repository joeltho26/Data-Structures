def linear_search(numbers,number_to_find):
    for idx in range(len(numbers)):
        if numbers[idx] == number_to_find:
            return idx

def binary_search(numbers,number_to_find):
    left_index = 0
    right_index = len(numbers) - 1
    mid_index = 0
    
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers[mid_index]
        
        if mid_number == number_to_find:
            return mid_index
        
        if number_to_find < mid_number:
            right_index = mid_index - 1
        elif number_to_find > mid_number:
            left_index = mid_index + 1
    
    return -1

def binary_search_recursive(numbers,number_to_find,left_index,right_index):
    if left_index > right_index or right_index < 0 or left_index < 0:
        return -1
    
    mid_index = (left_index + right_index) // 2
    mid_number = numbers[mid_index]
    
    if mid_number == number_to_find:
            return mid_index
        
    if number_to_find < mid_number:
        right_index = mid_index - 1
    elif number_to_find > mid_number:
        left_index = mid_index + 1
    
    return binary_search_recursive(numbers,number_to_find,left_index,right_index)

if __name__ == "__main__":
    numbers = [7,12,14,15,20,23,27,88]
    number_to_find = 27
    print(linear_search(numbers,number_to_find))
    print(binary_search(numbers,number_to_find))
    print(binary_search_recursive(numbers,number_to_find,0,len(numbers)-1))