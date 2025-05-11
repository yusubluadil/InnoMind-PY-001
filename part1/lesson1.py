print('Hello, world!') # Çap etmək


# Strings - Simvollar yığını
# '', "", '''''', """""" and str()

print('Adil')
'Yusublu'
"Innomind"

"Xoş gəldiniz, Renad bəy!"
"Xoş gəldiniz, Aygün xanım!"

# Multiline
'''
Adil
Yusublu
programmer
'''

"""Python
is a programming language"""

'''Guido Van Rossum'''

print(type(123)) # Integer
print(type(str(123))) # String


# +, *

print('Pro' + 'grammer') # Birlestirme
print("Python" * 3) # Tekrarlama



# Numerical Data Types

# Integer - Tam ədədlər
# Float - Onluq ədədlər
# Complex - Xəyali ədədlər

# Int
123
22
28
100
-200
0
10000

# Float
10.5
1.2
1.0
1.
125.
0.5
0.896
-0.5

# Complex
6 + 3j
2 - 2j

# Arithmetic Operators - Riyazi operatorlar
# +, -, *, /, //, %, **

print(915 + 758)
print(12745 - 598)
print(5.5 * 1.36)
print(4.5 / 3)
print(14 // 3)
print(14 % 3)
print(2 ** 3)


# 121-dən kökü necə ala bilərik?
print(121 ** 0.5)
print(121 ** (1 / 2))

# 27-dən 3-cü dərəcəli kökü
print(27 ** (1 / 3))


# Boolean - Doğru və ya Yalan
# True - Doğru
# False - Yalan

print(type('True')) # String
print(type(True)) # Boolean


# Comparison Operators - Müqayisə operatorları
print('#' * 50)
print(1 == 1) # Bərabərdir
print(1 == 2)

print(23 != 23) # Bərabər deyil
print(35 != 45)

print(12 > 14) # Böyükdür
print(12 >= 14) # Böyük və ya bərabərdir

print(12 < 14) # Kiçikdir
print(14 <= 14) # Kiçik və ya bərabərdir


# Variables - Dəyişənlər
# print(text) - Xətalıdır, çünki text dəyişəni təyin edilməyib
text = "Salam, mən python öyrənirəm!" # str
print(text)

print(id("Salam, mən python öyrənirəm!")) # str
print(id("Salam, mən python öyrənirəm"))# str
print(id(text))

# Iki və daha artıq Sözdən ibarət dəyişənləri təyin edərkən altdan xətt (_)
# istifadə edirik!
# Dəyişənlər böyük və kiçik hərflərə həssasdır!
say_hi = 'Salam' # str

my_name = "Adil" # str
print(my_name)
