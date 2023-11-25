def linear_search(arr, target):
    index = -1
    for i in range(len(arr)):
        if arr[i] == target:
            index = i
            print("Axtardığımız ədədin indeksi:", index)
            break

    if index == -1:
        print("Ədəd tapılmadı.")


# Misal:
my_array = [28, 3, 11, 32, 6, 55, 10, 5]
my_target = 3

linear_search(my_array, my_target)
