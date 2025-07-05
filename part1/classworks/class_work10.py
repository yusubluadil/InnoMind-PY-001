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

def int_to_word(number):
    if number.isdigit():
        result = ''
        for i in number:
            if i == '0':
                result += 'Sıfır '
            elif i == '1':
                result += 'Bir '
            elif i == '2':
                result += 'Iki '
            elif i == '3':
                result += 'Üç '
            elif i == '4':
                result += 'Dörd '
            elif i == '5':
                result += 'Beş '
            elif i == '6':
                result += 'Altı '
            elif i == '7':
                result += 'Yeddi '
            elif i == '8':
                result += 'Səkkiz '
            else:
                result += 'Doqquz '
        print(result)
    else:
        print('Yalniz reqem daxil etmelisiniz!')


num = input('Rəqəmi daxil edin: ')
int_to_word(num)

# 12. Söz sıxlaşdırma funksiyası.
# "aaabbcccc" → "a3b2c4" şəklində sıxlaşdırma funksiyası yazın.


def compress_letter(string):
    data = dict()

    for letter in string:
        data[letter] = data.get(letter, 0) + 1

    result = ''
    for k, v in data.items():
        result += k
        result += str(v)
    print(result)


txt = input('Simvolları daxil edin: ')
compress_letter(txt)


# 13. Kalkulyator funksiyası.
# İki ədəd və bir operator qəbul edən (+, -, *, /) funksiyanı yazın.


def calculator(num1, num2, operation):
    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        if num2 == 0:
            print('Bölən 0 ola bilməz!')
        else:
            print(round(num1 / num2, 2))
    else:
        print('Yanlış əməliyyat!')

num1 = float(input('1-ci rəqəmi daxil edin: ')) # 12 -> 12.0
num2 = float(input('2-ci rəqəmi daxil edin: '))
operation = input('Əməliyyatı daxil edin: ')
calculator(num1, num2, operation)

# 14. Ədədi tarixə çevirən funksiya.
# Məsələn, "28062025" → "28 iyun 2025" formasında qaytarılsın.


def str_to_date(string):
    int_to_month = {
        '01': 'Yanvar',
        '02': 'Fevral',
        '03': 'Mart',
        '04': 'Aprel',
        '05': 'May',
        '06': 'Iyun',
        '07': 'Iyul',
        '08': 'Avqust',
        '09': 'Sentyabr',
        '10': 'Oktyabr',
        '11': 'Noyabr',
        '12': 'Dekabr'
    }
    months_31 = ['01', '03', '05', '07', '08', '10', '12']
    month_num = string[2:4]
    if month_num in int_to_month:
        if month_num in months_31:
            if int(string[0:2]) > 31:
                print('Tarix doğru deyil!')
            else:
                month = int_to_month.get(month_num)
                result = f'{string[0:2]} {month} {string[4:8]}'
                print(result)
        else:
            if month_num == '02':
                if int(string[4:8]) % 4 == 0:
                    if int(string[0:2]) > 29:
                        print('Tarix doğru deyil!')
                    else:
                        month = int_to_month.get(month_num)
                        result = f'{string[0:2]} {month} {string[4:8]}'
                        print(result)
                else:
                    if int(string[0:2]) > 28:
                        print('Tarix doğru deyil!')
                    else:
                        month = int_to_month.get(month_num)
                        result = f'{string[0:2]} {month} {string[4:8]}'
                        print(result)
            else:
                if int(string[0:2]) > 30:
                    print('Tarix doğru deyil!')
                else:
                    month = int_to_month.get(month_num)
                    result = f'{string[0:2]} {month} {string[4:8]}'
                    print(result)
    else:
        print('Tarix doğru deyil!')


date = input('Tarixi daxil edin(01012001): ')
str_to_date(date)
