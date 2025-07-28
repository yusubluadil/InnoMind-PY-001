# Conditions - if, elif, else

# if şərt:
#     # şərt doğru olarsa icra olunacaq blok
# elif şərt:
#     # şərt doğru olarsa icra olunacaq blok
# else:
#     # şərt doğru olmasa icra olunacaq blok


# Comparison operators # ==, !=, >, <, >=, <=

print(5 == 5)
print(5 > 3)

if 5 != 5:
    print('5 5-ə bərabərdir')

if 5 > 3:
    print('5 3-dən böyükdür')


# if False:
#     print('5 5-ə bərabərdir')

# if True:
#     print('5 3-dən böyükdür')



if 125 > -235.89:
    print(125)
else:
    print(-235.89)


if 45 <= 45:
    print(45)
else:
    print('səhvdir')


if 125 >= 569:
    print(125)
else:
    print(569)


if 'python' == 'python':
    print('python')
else:
    print('JS')


if 'python' != 'python':
    print('python')
else:
    print('JS')


num1 = int(input('Daxil edin: '))
num2 = int(input('Daxil edin: '))

if num1 > num2:
    print(f'{num1} {num2}-dən böyükdür')
elif num1 == num2:
    print(f'{num1} {num2}-ə bərabərdir')
else:
    print(f'{num2} {num1}-dən böyükdür')





# Python conditions - Part 2

# and -> və ("Vurma")

if 5 > 3 and 10 > 5:
    print('Hər iki şərt doğrudur')

if 5 > 3 and 10 < 5:
    print('Hər iki şərt doğrudur')


# or -> və ya ("Toplama")

# (1 or 1 = 1 + 1 = 1)
if 5 > 3 or 10 > 5:
    print('Hər iki şərt doğrudur')

if 5 > 3 or 10 < 5:
    print('Hər iki şərt doğrudur')


# in; not in - İterable obyektlərdə axtarış

county = 'Azerbaijan'
letter = input('Hərf daxil edin: ')

if letter in county:
    print(f'{letter} hərfi {county} adında mövcuddur.')
else:
    print(f'{letter} hərfi {county} adında mövcud deyil.')


numbers = [1, 2, 3, 4, 5]
num = int(input('Rəqəm daxil edin: '))

if num not in numbers:
    print(f'{num} listdə mövcud deyil.')
else:
    print(f'{num} listdə mövcuddur.')


# is; is not - Obyektin yaddaş ünvanını və dəyərini müqayisə edir.

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))

if a is b:
    print('a və b eynidir')

if a is not b:
    print('a və b eyni deyil')


empty = None # None - heç nə yoxdur, boşdur
print(type(empty))


a = None

if a is None:
    print('a boşdur')
elif a is not None:
    print('a boş deyil')



# nested conditions - iç içə şərtlər

# Istifadecinin daxil etdiyi reqemin 10-dan boyuk ve cut eded olmasini
# yoxlayan proqram.


num = int(input('Reqem daxil edin: '))

if num > 10:
    if num % 2 == 0:
        print(f'{num} 10-dan boyuk ve cut ededdir.')
    else:
        print(f'{num} 10-dan boyuk ve tek ededdir.')
else:
    print(f'{num} serti odemir.')


# if num > 10 and num % 2 == 0:
#     print(f'{num} 10-dan boyuk ve cut ededdir.')
# elif num > 10 and num % 2 != 0:
#     print(f'{num} 10-dan boyuk ve tek ededdir.')
# else:
#     print(f'{num} serti odemir.')
