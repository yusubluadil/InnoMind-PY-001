# 1.​ İstifadəçinin daxil etdiyi ədədin cüt və ya tək olduğunu 
# müəyyən edən proqram tərtib edin.


# number = int(input('Ədəd daxil edin: '))

# if number == 0:
#     print('Sıfır')
# elif number % 2 == 0:
#     print('Cüt ədəd')
# else:
#     print('Tək ədəd')



# 2. istifadəçi_adı = "admin" və parol = "12345" kimi
# məlumat var. İstifadəçinin daxil etdiyi istifadəçi adı və parol burda
# verilən məlumatlara bərabərdirsə, bu zaman xoş gəldiniz mesajı
# yazılsın. Əks halda, daxil edilən məlumatlar yanlışdır kimi mesaj
# verilsin.


# DB
username = "admin"
pswd = "12345"


# Input
input_username = input('İstifadəçi adınızı daxil edin: ')
input_pswd = input('Parolunuzu daxil edin: ')


# Checking
if input_username == username and input_pswd == pswd:
    print('Xoş gəldiniz!')
else:
    print('Daxil edilən məlumatlar yanlışdır!')
