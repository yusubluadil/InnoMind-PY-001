# Aşağıdakı kimi dəyişən adları təyin edə bilmərik!

# if = 'salam'
# elif = 12
# else
# def
# while
# for
# class
# vesair

# 12name = ''

# my-name = 'adil'

# my name

pi = 3.14
PI = 3.14 # Contstant variable


# Arithmetic operations - part 2

num1 = 10
num1 = num1 + 1 # num1 += 1
print(num1)
print('$' * 50)


# Strings - Part 2
# Stringler indexlenen data tipdir.
# Stringler deyisilmezdir.

prog_lang_name = 'Python'
print(prog_lang_name[0])

print(prog_lang_name[5])
print(prog_lang_name[-1])

# Stringlerin uzunluqu
print(len(prog_lang_name))
print(prog_lang_name[len(prog_lang_name) - 1])

# prog_lang_name[0] = 'Y' # Xətalı koddur.
prog_lang_name = prog_lang_name + ' programming'
prog_lang_name += ' programming'
print(prog_lang_name)
print('=' * 50)

# String methods

name = input('Adınızı daxil edin: ')
print(name.capitalize()) # ilk herfi boyudur!

prog_name = 'python_45'
print(prog_name.upper()) # Butun herfleri boyudur!

username = 'YusUboV'
username_lower = username.lower()
print(username.lower()) # Butun herfleri kiçik edir!

print(username.count('U'))
print(username_lower.count('U'))


# =============== Task 1 ===============

balans = 200
withdraw_amount = int(input('Mebleg daxil edin: '))
balans -= withdraw_amount
print('Mebleg: ', balans)
