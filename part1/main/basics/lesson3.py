# Str methods - Part 2 (Strings are immutable !!!) 

name = 'Adil'
surname = 'Yusublu'

# fullname = name + ' ' + surname
fullname = '{} {}'.format(name, surname)
print(fullname)

# fullname = '{1} {0}'.format(name, surname)
# print(fullname)

fullname = f'{name} {surname}' # f-string
print(fullname)


# casefold() - Butun herfleri kicildir.
print('ADIL'.casefold())

# endswith() - Sringin sonu verilmiş simvolla bitirilib-bitirilmədiyini yoxlayır.
# startwith() - Sringin əvvəli verilmiş simvolla başlayıb-başlamadığını yoxlayır.

print('Python'.endswith('txt'))
print('Python'.startswith('Py'))

# islower() - Butun herfleri kicikdirse, True qaytarır.
# isupper() - Butun herfleri boyukdurse, True qaytarır.

print('python'.islower())
print('PYTHON'.isupper())

# strip() - Stringin evvelinde ve sonunda olan bosluqlari silir.
# lstrip() - Stringin sol evvelinde olan bosluqlari silir.
# rstrip() - Stringin sag sonunda olan bosluqlari silir.

print('   python   '.strip() + '!')
print('   python   '.lstrip() + '!')
print('   python   '.rstrip())


# isalpha() - Butun simvollar herflerden ibaretdirse, True qaytarır.
# isdigit() - butun simvollar ededlerden ibaretdirse, True qaytarır.
# isalnum() - Butun simvollar herf ve ededlerden ibaretdirse, True qaytarır.

print('python'.isalpha())
print('123'.isdigit())
print('python123'.isalnum())


# replace() - Verilmiş simvolu dəyişdirir.
a = 'Python'
print(a.replace('o', 'a')) # Pythan
print(a)


# title() - Str daxilindeki butun sozlerin ilk herflerini boyudur!
txt = 'salam, men python oyrenirem!'
print(txt.title())


# split() - Stringi daxil edilmiş simvola gore parcalayir.
products = 'Alma,armud,banan'
products_list = products.split(',')

print(products)
print(products_list)


# join() - Stringi daxil edilmiş simvola gore birleşdirir.
products_list = ['Alma', 'armud', 'banan']
products = ' '.join(products_list)

print(products)
