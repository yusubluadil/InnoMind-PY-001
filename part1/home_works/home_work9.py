# 1.​ İstifadəçinin daxil etdiyi ədədin faktorialını hesablayan proqram
# tərtib edin. (Faktorial mövzusunu internetdən araşdıra bilərsiniz.)

# 5! = 5 * 4 * 3 * 2 * 1 (120)

# num = int(input('Ədədi daxil edin: '))

# result = 1


# for i in range(1, num + 1):
#     result = result * i

# print(f"{num}! = {result}")



# 2.​ İstifadəçinin daxil etdiyi ədədə kimi Fibonaççi ardıcıllığı yaradan
# proqram tərtib edin. (Ardıcıllıqda minimum iki rəqəm mövcuddur.
# Həmin rəqəmlər də 0 və 1-dir. Əlavə olaraq Fibonaççi ardıcıllığı
# haqqında internetdə araşdırma edə bilərsiniz.)

# 6
# 0, 1, 1, 2, 3, 5

# element_count = int(input('Ədədi daxil edin: '))

# if element_count < 2:
#     print('Minimum 2 daxil edilməlidir!')
# else:
#     fibo_list = [0, 1]

#     counter = 1
#     while counter <= element_count - 2:
#         element = fibo_list[counter] + fibo_list[counter - 1]
#         fibo_list.append(element)

#         counter += 1

#     print(fibo_list)



# 3.​ İstifadəçinin daxil etdiyi ədədin sadə olub-olmadığını müəyyən
# edən proqram tərtib edin. (Yalnız 1-ə və özünə bölünən ədədlərə
# sadə ədədlər deyilir.)


# number = int(input('Ədədi daxil edin: '))
# count = 0

# for i in range(1, number + 1):
#     if number % i == 0:
#         count += 1

# if count == 1:
#     print('1 nə sadədir, nə də mürəkkəb!')
# elif count == 2:
#     print(f'{number} ədədi sadə ədəddir!')
# else:
#     print(f'{number} mürəkkəb ədəddir!')




# 4.​ İstifadəçinin daxil etdiyi ədədin bütün bölənlərini list şəklində çap
# edən və sayını göstərən proqram tərtib edin. (Məsələn, 6 daxil edilərsə, nəticə olaraq
# [1, 2, 3, 6] verilməlidir.)


# number = int(input('Ədədi daxil edin: '))
# nums = []

# for i in range(1, number + 1):
#     if number % i == 0:
#         nums.append(i)

# print(nums)

# print(len(nums))
