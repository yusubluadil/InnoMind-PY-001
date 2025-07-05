# # Functions

# # def - Açar sözü vasitəsilə təyin olunur.
# # def func_name():
# #   function body


# def print_renad():
#     print('Renad')


# print_renad()


# # 1. Kvadrat hesablayan funksiya yazın.
# # İstifadəçi bir ədəd daxil edir, funksiya onun kvadratını qaytarır.

# def kvadrat():
#     number = int(input('Bir ədəd daxil edin: '))
#     print(number ** 2)

# kvadrat()


# # 2. Salamlaşma funksiyası.
# # Adı qəbul edən funksiya "Salam, Adil!" kimi mesajı çap etsin.


# def say_hi():
#     name = input('Adı daxil edin: ')
#     print(f'Salam, {name}!')

# say_hi()


# # Built in functions
# # print()
# # input()
# # sorted()


# # Function with parametrs

# # Argument - Funksiyaya göndərilən dəyərlər
# # Parametr - Funksiya təyin olunduğu zaman mötərizədə yazılanlar

# print('salam') # Arguments
# input('Metni daxil edin') # Arguments
# sorted([3, 2, 5, 4, 79, 34]) # Arguments


# # def func_name(num1, num2):
# #   print(num1 + num2)


# def sum_two_nums(n1, n2):
#     print(n1 + n2)


# sum_two_nums(1, 2)


# # Daxil edilmiş radiusa görə dairənin
# # sahə və perimetrini hesablayan func yazın.

# # S = pi x R^2
# def square(radius):
#     print(3.14 * radius ** 2)

# r = 2

# square(r)


# # P = 2 x pi x R
# # perimeter

# def perimeter(r):
#     print(round((2 * 3.14 * r), 2))

# perimeter(5)



# Default arguments
def say_hi(name1, name2='Renad', name3='Aygün'):
    print(f'Salam {name1}, {name2} və {name3}')

say_hi(name1='Adil', name2='Nihat', name3='Orxan') # Keyword arguments
say_hi('Adil', 'Nihat', 'Orxan') # Positional arguments


def change_currency(amount=0, curr=None):
    if curr is None:
        print('Valyutanı daxil edin.')
    elif curr == 'usd':
        print(round(amount / 1.7, 2))


change_currency(curr='usd')


# *args - istənilən sayda Positional Arguments,
# **kwargs - istənilən sayda keyword Arguments


# 8. Ən böyük ədədi tapan funksiya.
# İstənilən sayda arqument qəbul edib ən böyüyünü tapın.

def get_max_value(*args):
    max_value = max(args)
    print(max_value)

# Aşağıdakı kod xəta verəcək. Çünki ən sonda keyvord arqument göndərilib
# get_max_value(1, 2, 3, 56, 2, 12, 45, 76590, 89, integer=45)
get_max_value(1, 2, 3, 56, 2, 12, 45, 76590, 89)


def get_info(**kwargs):
    print(kwargs)


get_info(name='adil', age=22)
# get_info('adil') # Xətalıdır. Çünki, funksiya yalnız keyvord arqument qəbul edir.



# Return - funksiyadan əldə olunan nəticəni funksiyanın özünə mənimsədərək
# funksiyanı bölür.


def multiply(n1, n2):
    return n1 + n2

print(multiply(1, 2))

