# Functions

# def - Açar sözü vasitəsilə təyin olunur.
# def func_name():
#   function body


def print_renad():
    print('Renad')


print_renad()


# 1. Kvadrat hesablayan funksiya yazın.
# İstifadəçi bir ədəd daxil edir, funksiya onun kvadratını qaytarır.

def kvadrat():
    number = int(input('Bir ədəd daxil edin: '))
    print(number ** 2)

kvadrat()


# 2. Salamlaşma funksiyası.
# Adı qəbul edən funksiya "Salam, Adil!" kimi mesajı çap etsin.


def say_hi():
    name = input('Adı daxil edin: ')
    print(f'Salam, {name}!')

say_hi()


# Built in functions
# print()
# input()
# sorted()


# Function with parametrs

# Argument - Funksiyaya göndərilən dəyərlər
# Parametr - Funksiya təyin olunduğu zaman mötərizədə yazılanlar

print('salam') # Arguments
input('Metni daxil edin') # Arguments
sorted([3, 2, 5, 4, 79, 34]) # Arguments


# def func_name(num1, num2):
#   print(num1 + num2)


def sum_two_nums(n1, n2):
    print(n1 + n2)


sum_two_nums(1, 2)


# Daxil edilmiş radiusa görə dairənin
# sahə və perimetrini hesablayan func yazın.

# S = pi x R^2
def square(radius):
    print(3.14 * radius ** 2)

r = 2

square(r)


# P = 2 x pi x R
# perimeter

def perimeter(r):
    print(round((2 * 3.14 * r), 2))

perimeter(5)


# 8. Ən böyük ədədi tapan funksiya.
# İstənilən sayda arqument qəbul edib ən böyüyünü tapın.
