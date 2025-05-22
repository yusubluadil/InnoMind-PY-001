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
