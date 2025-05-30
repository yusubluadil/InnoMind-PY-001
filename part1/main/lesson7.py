# Tuple - Müxtəlif məlumatları özündə saxlayan data tipdir.
# Tuple yalnız python-da mövcuddur.
# Tuple dəyişilməzdir. (immutable)
# Tuple sıralıdır. (ordered)
# Tuple indekslənəndir.


tpl = (1, 2, 3, 4, 5)
print(type(tpl)) # <class 'tuple'>


lst = [1, 2, 3, 4, 5]
tpl2 = tuple(lst)
tpl3 = tuple("Hello")

# tpl3 = tuple("Hello", "world") # Xətalıdır.
# tpl3 = tuple(("Hello", "world")) # Düzgündür
# tpl3 = tuple(["Hello", "world"]) # Düzgündür

print(tpl2)  # (1, 2, 3, 4, 5)
print(tpl3)  # ('H', 'e', 'l', 'l', 'o')


mixed_tuple = (1, "Hello", 3.14, True, None, ['salam', 'dunya'], (5, 4, 3))

print(mixed_tuple)

print(mixed_tuple[0])
print(mixed_tuple[1][-1])
print(mixed_tuple[-1][1])
print(mixed_tuple[-2][0][1])

print(mixed_tuple[:3])
print(mixed_tuple[::2])


# a = (1, 2, 3, 4, 5)
# a[0] = 10          # Xetali koddur
# print(a)


a = ['Python']
print(a)
print(len(a))
print(type(a))

# QEYD: TUPLE TƏMSİL EDƏN MÖTƏRİZƏ YOX, VERGÜLDÜR.
b = ('Python',)
print(b)
print(len(b))
print(type(b))


my_tpl = 1, 2, 3, 4, 5
print(my_tpl)
print(type(my_tpl))


# index, name = 1, 'Adil'

# print(index)
# print(name)


# name = surname = 'Huseyn'

# print(name)
# print(surname)



a = (1, 2, 3)
b = (4, 5, 6)

print(a + b)

print(a * 3)


# Tuple methods

names = ('Adil', 'Huseyn', 'Elvin', 'Aysel', 'Elvin')
print(names.count('Elvin'))  # 2

print(names.index('Aysel'))  # 3



# print() - Parameters (sep, end)

print('Salam', 'Dunya', 'Necesen', sep='-')

print('Salam', end=' ')
print('Dunya', end=' ')
print('Necesen')
