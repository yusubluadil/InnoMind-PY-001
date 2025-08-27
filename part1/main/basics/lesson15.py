# Python packages
# Virtual environment
# Third party packages (pip) [requests modulu üzərindən izah]

# Decorator
# Generator


# Python packages - Tərkibində bir neçə modul mövcud olur.
import time

from package import *

func1()
func2()
# secret_func()



# Virtual environment - Virtual mühit (Versiya toqquşmalarının qarşısını almaq üçün istifadə olunur.)
# Third party packages (pip) [requests modulu üzərindən izah]

# Virtual mühit yaratmaq üçün - [python -m venv <folder_name>]
# Virtual mühiti aktivləşdirmək üçün - [<folder_name>\Scripts\activate]
# 3-cü tərəf paket quraşdırmaq üçün - [pip install <package_name>]

# Digər terminal komandaları
# cd <folder_name> - (Change Directory) [folder_name adlı qovluğa keçid edir]
# cd .. - [Bir üst qovluğa qayıdır]
# dir - [Qovluğun içində olan fayl və folderləri göstərir]
# cls - [Terminalı təmizləyir]
# mkdir <folder_name> - [<folder_name> adlı qovluq yaradır]
# code . - [İçində olduğumuz qovluğu VScode-da açır]


# Decorator - Funksiyaya birbaşa müdaxilə etmədən funksiyanın nəticəsinin dəyişdirilməsi
# Decorator-lar da funksiyadır. Decoratorlar arqument kimi fərqli bir func alır.


def make_log(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} adlı funksiya başladı.")
        func(*args, **kwargs)
        print(f"{func.__name__} adlı funksiya dayandı.")
    return wrapper

@make_log
def say_hi():
    print('salam')

say_hi()


def get_execute_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()

        result = end_time - start_time
        print(f'{func.__name__} adlı funksiya {result} saniyə ərzində icra olundu.')
    return inner


@get_execute_time
def example_func():
    for i in range(100):
        print(i)


example_func()









# generator - Yaddaşa qənaət etmək üçün istifadə olunur.

def get_nums():
    nums = []
    for i in range(1000):
        nums.append(i)

    return nums


def get_nums_generator():
    for i in range(1000):
        yield i

my_gen = get_nums_generator()

print(get_nums())
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))


import sys

def normal_squares(n):
    return [i*i for i in range(n)]

def generator_squares(n):
    for i in range(n):
        yield i*i

n = 10**6

normal = normal_squares(n)
generator = generator_squares(n)

print("Normal list memory:", sys.getsizeof(normal))
print("Generator memory  :", sys.getsizeof(generator))
