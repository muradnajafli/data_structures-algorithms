def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Massivin ortasını tapmaq

        if arr[mid] == target:
            return mid  # Element tapıldı, indeksini qaytar
        elif arr[mid] < target:
            low = mid + 1  # Hədəf element sağdadı, axtarma aralığını daralt
        else:
            high = mid - 1  # Hədəf element soldadı, arama aralığını daralt

    return -1  # Element massivdə tapılmadı


# Misal:
my_array = [7, 12, 14, 22, 26, 30, 32]
result = binary_search(my_array, 12)
print(result)
