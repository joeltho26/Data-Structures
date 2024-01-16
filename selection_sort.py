def selection_sort(numbers):
    size = len(numbers)
    for i in range(size -1):
        min_index = i
        for j in range(min_index+1,size):
            if numbers[j] < numbers[min_index]:
                min_index = j
        if i != min_index:
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

if __name__ == "__main__":
    numbers = [15,12,7,88,14,27,20,23]
    selection_sort(numbers)
    print(numbers)