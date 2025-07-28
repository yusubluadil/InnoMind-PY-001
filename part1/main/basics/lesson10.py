# Set - Riyzai olaraq çoxluqlar deməkdir.
# Set - Sırasızdır.
# Set - İndex-lənmir.
# Set - For loop vasitəsi ilə üzərində gəzinə bilərik.
# Set - Dəyişməzdir.
# Set - Daxilində olan dəyərlər unikaldır (Yəni, təkrarlanmır.).

# empty_set = set() # Boş set yaratmaq üçün
# a = set([1, 2, 3, 4, 'salam'])
# b = {1, 2, 3, 4, 'salam', 'python', 5}


a = {1, 2, 3}
b = {3, 4, 5}

# add() - Element əlavə edir.
a.add(4)
print(a)

# remove() - Dəyərinə görə element silir. (Element olmazsa, xəta verəcək.)
a.remove(4)
print(a)

# discard() - Dəyərinə görə element silir. (Element olmazsa, heç bir əməliyyat icra etməyəcək.)
a.discard(5)
print(a)


# - (İki set)
diff = a - b
print(diff)
print(a.difference(b))

# & (Ortaq elementləri göstərir)
c = a & b
print(c)
print(a.intersection(b))

# | (Birləşdirmə)
c = a | b
print(c)
print(a.union(b))


# ^ (a-nın b-dən və b-nin a-dan fərqini göstərir)
c = a ^ b
print(c)
print(a.symmetric_difference(b))



x = {1, 2, 3, True}
print(x)

y = {1, 3, 0, 2, False}
print(y)


for i in y:
    print(i)
