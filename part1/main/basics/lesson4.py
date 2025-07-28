# List (Array) - Müxtəlif məlumatları özündə saxlayan data tipdir.
# Listlər sıralıdır (ordered).

my_lst = [] # my_lst = list()

lst = ['Python', 'Java', 'C#', 'C++', 'JavaScript']

print(lst)
print(type(lst))

# List-lər indekslənəndir!

print(lst[0]) # Python
print(lst[0][0]) # P

print(lst[2]) # C#

print(lst[-1]) # JavaScript
print(lst[-2]) # C++

print(lst[0:3])

print(lst[::-1])


# Listlər dəyişiləndir! (mutable)

lst[0] = 'Golang'

print(lst)

# List-lərin uzunluqu

print(len(my_lst))
print(len(lst))

# Fərqli data tiplərdən ibarət list

mixed_list = ['Adil', 123, 3.14, True, 3 + 2j, [1, 'Salam']]

print(mixed_list[-1])
print(type(mixed_list[-1]))

print(mixed_list[-1][-1][-1])


# List-lərin metodları

# append() - Listin sonuna element əlavə edir.

print('=' * 50)

names = ['Adil', 'Orxan']
print(names)

names.append('Nihat')
print(names)

# insert() - Daxil etdiyimiz indeksə elementi əlavə edir.
names.insert(0, 'Ruslan')
print(names)

# clear() - Listi təmizləyir.
names.clear()
print(names)
