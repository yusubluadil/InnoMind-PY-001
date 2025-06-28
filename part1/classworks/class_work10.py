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


# 3. Ədədlərin cəmini tapan funksiya.
# İki ədəd qəbul edən funksiya onların cəmini qaytarsın.

def sum_two_nums(n1, n2):
    print(n1 + n2)


sum_two_nums(1, 2)


# 4. Cüt və ya tək olduğunu yoxlayan funksiya.
# Bir ədəd daxil edilir, funksiya onun cüt və ya tək olduğunu qaytarır.

def even_or_odd(number):
    if number % 2 == 0:
        print('Cüt')
    else:
        print('Tək')

even_or_odd(5)


# 5. Dərəcədən Fahrenheitə çevirən funksiya.
# (C * 9/5) + 32 düsturundan istifadə edin.

def celsius_to_fahrenheit(celsius):
    print((celsius * (9 / 5)) + 32)

celsius_to_fahrenheit(30)


# 6. Faktorial hesablayan funksiya.
# Dövr (loop) ilə yazın.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    print(result)

num = int(input('ədədi daxil edin: '))

factorial(num)


# 7. Palindrome yoxlayan funksiya.
# Daxil edilən söz tərsinə oxunduqda da eyni qalırmı?

def palindrome(word):
    if word == word[::-1]:
        print('Palindrome')
    else:
        print('Palindrome deyil')

palindrome('sus')


# 9. Sadə ədəd olub-olmadığını yoxlayan funksiya.
# Ədədin yalnız 1 və özünə bölünüb-bölünmədiyini yoxlayın.

def simple_or_complex(n):
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count >= 2:
        print(f'{n} sadə ədəddir.')
    else:
        print(f'{n} mürəkkəb ədəddir.')

simple_or_complex(17)


# 10. Ədədlər siyahısındakı cüt ədədləri qaytaran funksiya.

def even_nums(numbers):
    result = []
    for i in numbers:
        if i % 2 == 0:
            result.append(i)

    print(result)

numbers = [13, 24, 45, 37, 23, 45, 12, 90, 2, -8, 52]
even_nums(numbers)


# 11. Rəqəmlərin sözlə ifadəsi.
# 123 → bir iki üç kimi sözlərlə qaytarılsın.

# 12. Söz sıxlaşdırma funksiyası.
# "aaabbcccc" → "a3b2c4" şəklində sıxlaşdırma funksiyası yazın.

# 13. Kalkulyator funksiyası.
# İki ədəd və bir operator qəbul edən (+, -, *, /) funksiyanı yazın.

# 14. Ədədi tarixə çevirən funksiya.
# Məsələn, 28062025 → "28 iyun 2025" formasında qaytarılsın.
