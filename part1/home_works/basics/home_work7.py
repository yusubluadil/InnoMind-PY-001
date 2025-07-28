# 1.​ İstifadəçi 5 element daxil edir. Həmin elementlərdən ibarət tuple
# yaradan və uzunluğunu çap edən proqram yazın.

a = input('Element 1: ')
b = input('Element 2: ')
c = input('Element 3: ')
d = input('Element 4: ')
e = input('Element 5: ')


my_tpl = (a, b, c, d, e)
print(my_tpl)

print(len(my_tpl))

# 2.​ İstifadəçinin daxil etdiyi ad, soyad və yaşdan ibarət dict təyin edən
# proqram yazın.


name = input('Ad: ')
surname = input('Soyad: ')
age = input('Yaş: ')

user = {'name': name}
user['surname'] = surname
user['age'] = age


user_info = {
    'name': name,
    'surname': surname,
    'age': age
}

print(user)



# 3. person = ("Adil", 22, "Bakı") kimi bir tuple var. Tuple unpacking
# istifadə edərək person daxilindəki elementləri ayrı-ayrı dəyişənlərə
# mənimsədin.

person = ("Adil", 22, "Bakı")

name, age, city = person

print(age)



# 4. scores = {"math": 90, "physics": 85, "chemistry": 78} kimi dict
# verilmişdir. Bu dict daxilində olan dəyərlərin cəmini və ədədi
# ortasını tapan proqram tərtib edin.


scores = {"math": 90, "physics": 85, "chemistry": 78}


list_scores = list(scores.values())

sum_scores = sum(list_scores)
avarage = sum_scores / len(list_scores)

print(sum_scores, round(avarage, 2))
print(f"{sum_scores}, {avarage:.2f}")
