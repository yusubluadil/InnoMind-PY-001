# List methods - Part 2

# copy() - Listi kopyalayır.

programming_names = ['Python', 'Java', 'C#', 'C++', 'JavaScript']
copied_list = programming_names.copy()

programming_names.append('Golang')

print(programming_names)
print(copied_list)


# count() - Daxil edilən elementin sayını göstərir.
fruits = ['apple', 'banana', 'cherry', 'apple', 'banana', 'apple']
print(fruits.count('apple'))

# index() - Daxil edilən elementin indeksini göstərir.
print(fruits.index('apple'))
print(fruits.index('apple', 1))
print(fruits.index('apple', 4))


# extend() - Listləri birləşdirir.
programming_names.extend(fruits)
print(fruits)
print(programming_names)

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
# all_nums = nums1 * 3 # Listi 3 dəfə təkrarlayır
all_nums = nums1 + nums2 # Listləri birləşdirir
print(all_nums)

print('=' * 50)

# remove() - Daxil edilən elementi `dəyərinə görə` listdən silir.

countries = ['USA', 'Canada', 'Mexico', 'USA', 'Germany']
print(countries)
a = countries.remove('USA')
# countries.remove('Turkey') # Xetali
print(countries)

# countries.clear()
# print(countries)


# pop() - Daxil edilən `indekse görə` elementi silir.
countries = ['USA', 'Canada', 'Mexico', 'USA', 'Germany']
deleted_country = countries.pop(0)

print(countries)
print(deleted_country)


# reverse() - Listi tərsinə çevirir.

cars = ['BMW', 'Mercedes', 'Audi', 'Toyota']

cars.reverse()
print(cars)


# sort() - Listi sıralayır.

grades = [90, 85, 95, 80, 70]
print(grades)
grades.sort()
grades.sort(reverse=True) # Tersine siralayir
print(grades)
