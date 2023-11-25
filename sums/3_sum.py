def three_sum(arr, arr_size, target_sum):
    for i in range(0, arr_size - 2):
        for j in range(i + 1, arr_size - 1):
            for k in range(j + 1, arr_size):
                if arr[i] + arr[j] + arr[k] == target_sum:
                    # Tapılan üçlünün indekslerini döndür
                    return [i, j, k]

    # Əgər üçlü cəmi əldə edə bilmədiksə, None qaytar
    return None


# Misal:
my_array = [1, 4, 45, 6, 10, 8]
my_target_sum = 22
my_arr_size = len(my_array)

result_indices = three_sum(my_array, my_arr_size, my_target_sum)

if result_indices:
    print(f"Üç elementin indeksləri: {result_indices}")
else:
    print("Üç element tapılmadı.")
