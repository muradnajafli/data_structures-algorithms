def two_sum(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]  # İki element tapdıq
        elif current_sum < target:
            left += 1  # Cəmi artırmaq üçün sol göstəricini hərəkət etdir
        else:
            right -= 1  # Cəmi azaltmak üçün sağ göstəricini hərəkət etdir

    return []  # İki element tapılmadı


# Misal:
my_nums = [2, 5, 11, 15]  # sıralı massiv istifadə etmək lazımdır.
my_target = 7

result = two_sum(my_nums, my_target)

if result:
    print(f"İki elementin indeksləri: {result}")
else:
    print("İki element tapılmadı.")
