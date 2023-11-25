def one_sum(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid  # Hədəf ədədi tapdıq
        elif nums[mid] < target:
            left = mid + 1  # Hədəf ədəd sağ tərəfdə olmalıdı
        else:
            right = mid - 1  # Hədəf ədəd sol tərəfdə olmalıdı

    return -1  # Hədəf ədəd tapılmadı


# Misal:
my_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # sıralı massiv istifadə etmək lazımdır.
my_target = 7

result = one_sum(my_nums, my_target)

if result != -1:
    print(f"Hədəf elementin indeksi: {result}")
else:
    print("Hədəf element tapılmadı.")
