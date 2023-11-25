def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(arr[min_index])


# Misal:
my_array = [64, 25, 31, 6, 57, 54]
selection_sort(my_array)
print(my_array)
