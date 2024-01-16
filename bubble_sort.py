def bubble_sort(numbers):
    size = len(numbers)
    for i in range(size - 1):
        swapped = False
        for j in range(size -i -1):
            if numbers[j] > numbers[j+1]:
                tmp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = tmp
                swapped = True
        
        if not swapped:
            break

if __name__ == "__main__":
    numbers = [15,12,7,88,14,27,20,23]
    bubble_sort(numbers)
    print(numbers)
    