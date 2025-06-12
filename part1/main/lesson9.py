# Loop - Dövr, döngü

# For loop - Iterable elementlər üzərində dövr qurmaq üçün istifadə olunur.

# for element in iterable:
#     məntiq

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for number in numbers:
#     if number % 2 == 0:
#         print(number)

even_nums = []
odd_nums = []

for number in numbers:
    if number % 2 == 0:
        even_nums.append(number)
    else:
        odd_nums.append(number)

print(even_nums)
print(odd_nums)

# Qeyd for loop ilə adətən i, j, k kimi dəyişənlər istifadə olunur.



# range() - 0-dan başlayaraq müəyyən bir sayda ədədlər yaratmaq üçün istifadə olunur.
# range(start, stop, step)

# for i in range(0, 20, 3):
#     print(i)

even_nums = []
odd_nums = []

for i in range(1, 100):
    if i % 2 == 0:
        even_nums.append(i)
    else:
        odd_nums.append(i)


print(even_nums)
print('-'*100)
print(odd_nums)
