"""
Doğum Gününə neçə gün qaldığını hesablayan proqram tərtib
edin. İstifadəçi doğum tarixini daxil edəcək. İstifadəçinin doğum
gününə neçə gün qaldığı çap olunacaq.
"""
import random

from string import (
    ascii_letters,
    digits,
    punctuation
)

from datetime import datetime

# 14.12.2002

today = datetime.today().date()

birth_date = '22.08.2005'


# print(type(birth_date), birth_date)
birth_date = datetime.strptime(birth_date, '%d.%m.%Y').date()
# print(type(birth_date), birth_date)

diff = 0
if today.month >= birth_date.month:
    if today.day > birth_date.day:
        birth_date = birth_date.replace(year=today.year + 1)
        diff = (birth_date - today).days
    else:
        birth_date = birth_date.replace(year=today.year)
        diff = (birth_date - today).days
else:
    birth_date = birth_date.replace(year=today.year)
    diff = (birth_date - today).days

if diff == 0:
    print('Təbriklər bu gün doğum gününüzdür!!!')
else:
    print(diff)



"""
Bugünkü Tarixi Çap edən proqram tərtib edin. Proqram hər işə
düşdüyü zaman cari günü print edəcək.
"""

str_today = datetime.strftime(today, '%d-%m-%Y')
print(str_today)


"""
İstifadəçi iki tarix daxil edəcək və onlar arasında olan gün fərqini
çap edən proqram tərtib edin.
"""

# date1 = input('1-ci tarixi daxil edin (GG-AA-İİİİ): ')
# date2 = input('2-ci tarixi daxil edin (GG-AA-İİİİ): ')


# dt1 = datetime.strptime(date1, '%d-%m-%Y')
# dt2 = datetime.strptime(date2, '%d-%m-%Y')

# diff = abs((dt1 - dt2).days)
# print(diff)



"""
İstifadəçinin daxil etdiyi tarix həftənin hansı gününə düşürsə, onu
çap edən proqram tərtib edin.
"""

# input_date = input('Tarixi daxil edin (GG-AA-İİİİ): ')

# dt = datetime.strptime(input_date, '%d-%m-%Y')
# weekday = datetime.strftime(dt, '%A')

# print(weekday)


"""
Parol yaradan proqramı qurun. İstifadəçi parol üçün uzunluq daxil
edəcək. Həmin uzunluqda təsadüfi seçilmiş müxtəlif simvollardan
ibarət parol yaradılaraq çap olunacaq.
"""

length = int(input('Parol uzunluğunu daxil edin: '))

symbols = ascii_letters + digits + punctuation

result_lst = random.choices(symbols, k=length)

pswd = ''.join(result_lst)

if length < 8:
    print('Xəbərdarlıq! 8 simvoldan aşağı parollar etibarlı sayılmır.')

print(pswd)
