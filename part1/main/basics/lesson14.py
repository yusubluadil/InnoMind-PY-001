# Working with files

import os # Operation System

"""
r - read - Faylları yalnız oxumaq üçündür.
(Fayl yoxdursa, xəta verir.)

w - write - Faylları yalnız yazmaq üçündür. (Faylın içindəki məlumat silinir və yenidən yazılır.)
(Fayl yoxdursa, yenisini yaradacaq.)

a - append - Faylları yalnız yazmaq üçündür. (Faylın köhnə məzmunu qalır.)
x - Yalnız fayl yaratmaq üçündür. (Əgər fayl varsa, xəta verir.)
b - binary - Şəkil, video, və s. bu tipli fayllar üçündür.
"""

file = open('part1/main/info.txt', encoding='utf-8', mode='r')

print(file.read()) # faylı oxuyur.
file.seek(0) # Cursoru ən başa qaytarır

print(file.readline()) # Faylda olan sətri oxuyur.
file.seek(0) # Cursoru ən başa qaytarır

print(file.readlines()) # Faylda olan məlumatları list şəklində qaytarır. 

file.close()
# print(file.readlines()) # Xəta verəcək. Çünki, fayl bağlıdır.



user_file = open('part1/main/user.txt', mode='w', encoding='utf-8')

user_file.write('Ad: Renad\nSoyad: Xasayev')
user_file.write('\n')
user_file.write('Ad: Aygün\nSoyad: Ağazadə')

# user_file.seek(0)
# user_file.read() # bu xəta verəcək. Çünki, fayl oxunma rejimində deyil.

user_file.close()



log_file = open('part1/main/logging.txt', mode='a', encoding='utf-8')

log_file.write('adil - sistemə daxil oldu - [23.07.2025 21:17]')
log_file.write('\n')

log_file.close()



if os.path.exists('part1/main/logging2.txt'):
    print('fayl mövcuddur!')
else:
    log_file2 = open('part1/main/logging2.txt', mode='x')
    log_file.close()
    print('Fayl yaradıldı.')



if os.path.exists('part1/main/log'):
    print('Qovluq mövcuddur!')
else:
    os.mkdir('part1/main/log', )
    print('Qovluq yaradıldı.')
