# Exception - İstisna

# 0 - a bölmə zamanı ZeroDivsionError istisnası qalxır.
# Təyin olunmamış dəyişənə müraciət etdiyimiz zaman NameError istisnası qalxır.

# try:
#   xətalı kod yazılır.
# except: (Xəta baş verərsə, icra olunur.)
#   Xəta baş verən zaman hansı əməliyyat olacağını təyin edirik.
# finally: (Xəta baş versədə, verməsədə bu blok icra olunacaq)
#   Hər zaman işə düşən blok


try:
    print(5 / 0)
except:
    print('0-a bölmək qadağandır.')


try:
    print(txt)
except:
    print('Daxil edilmiş dəyişən mövcud deyil!')
finally:
    print('Hər zaman dəyişən təyin edildikdən sonra müraciət olunmalıdır.')


try:
    print(int('123'))
except:
    print('int funksiyasına yanlış arqument göndərilib.')
finally:
    print('Düzgün yazılış qaydası int(numeric) kimidir.')


try:
    print(40 / 0)
    print(name)
except ZeroDivisionError:
    print('0-a bolmek qadagandir.')
except NameError:
    print('Dəyişəni təyin edin.')


try:
    print(7 + '7')
except (ZeroDivisionError, NameError, TypeError):
    print('0-a bolmek qadagandir. Dəyişəni təyin etmək lazımdır.')
    print('Tip xətası mövcuddur')


try:
    print(7 + 'salam')
except Exception as e:
    print('Exception: ', e)


num1 = int(input('Bölünəni daxil edin: '))
num2 = int(input('Böləni daxil edin: '))

if num2 == 0:
    raise Exception("Bölən 0 daxil edilə bilməz.")
