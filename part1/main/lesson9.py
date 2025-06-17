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

# print(even_nums)
# print(odd_nums)

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


# print(even_nums)
# print('-' * 100)
# print(odd_nums)


# while loop - Şərtli dövr.
# Müəyyən bir şərt doğru (True) olduğu müddət ərzində davam edəcək.

# while condition:
#   ...


# counter = 0
# while counter <= 25:
#     print(counter)
#     counter += 2


# for i in range(0, 25, 2):
#     print(i)

# for i in range(0, 25):
#     if i % 2 == 0:
#         print(i)


# continue, break - Uyğun olaraq davam et və sonlandır deməkdir.

# for i in range(0, 25):
#     if i % 2 == 1:
#         continue
#     print(i)


# counter = 0
# while counter < 10:
#     if counter == 5:
#         break
#     print(counter)

#     counter += 1



# while True - praktiki olaraq izahı
# kiçik kalkulyator app

while True:
    print("""
    +, -, *, /
    q - Proqramı sonlandır
""")

    operation = input('Əməliyyatı daxil edin: ')

    if operation == 'q':
        print('Proqram sonlandı...')
        break
    else:
        num1 = int(input('1-ci rəqəmi daxil edin: '))
        num2 = int(input('2-ci rəqəmi daxil edin: '))

        if operation == '+':
            print(num1 + num2)
        elif operation == '-':
            print(abs(num1 - num2))
        elif operation == '*':
            print(num1 * num2)
        elif operation == '/':
            if num2 == 0:
                print('0-a bölmə əməliyyatı mümkün deyil!')
                continue
            print(num1 / num2)
        else:
            print('Daxil etdiyiniz əməliyyat yanlışdır.')
