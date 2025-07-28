# 1. İstifadəçi yaş daxil edir və həmin yaşa görə istifadəçinin
# uşaq, yeniyetmə, gənc, orta yaşlı və ya yaşlı olduğunu müəyyən edən proqram yazın.


# age = int(input('Yaşınızı daxil edin: '))

# if age <= 6:
#     print('Uşaq')
# elif age <= 18:
#     print('Yeniyetmə')
# elif age <= 30:
#     print('Gənc')
# elif age <= 50:
#     print('Orta yaşlı')
# elif age <= 70:
#     print('Yaşlı')
# else:
#     print('Çox yaşlı')


# 2. İstifadəçinin daxil etdiyi ədədin müsbət, mənfi və ya sıfır olduğunu 
# müəyyən edən proqram yazın.

# 3. Tələbənin imtahan nəticəsini yoxlayan proqram yazın.
# (51-den kicik olarsa, kesilib. eks halda ise kecib)

# 4. İstifadəçidən 3 ədəd daxil etməsini istəyin. Bu 3 ədədin ən böyük olanını 
# müəyyən edən proqram yazın. # and == Arasdirmali task ==


# num1 = int(input('Birinci ədəd: '))
# num2 = int(input('Ikinci ədəd: '))
# num3 = int(input('Ucuncu ədəd: '))

# # 5 >= 4 and 5 >= 3 (1 * 1 = 1) ---> True
# if num1 >= num2 and num1 >= num3:
#     print(f'Ən böyük ədəd: {num1}')
# elif num2 >= num1 and num2 >= num3:
#     print(f'Ən böyük ədəd: {num2}')
# else:
#     print(f'Ən böyük ədəd: {num3}')

# 5. 51-61 (E), 61-71 (D), 71-81 (C), 81-91 (B), 91-100 (A) qiymət sistemini
# tətbiq edən proqram yazın. (İstifadəçi balı daxil edəcək.)

# Bug - Proqram işləyir, amma, nəticələr səhvdir.
# Error - Proqram çökür.

grade = int(input('Balınızı daxil edin: '))

# if grade >= 91 and grade <= 100:
#     print('A')
# elif grade >= 81 and grade < 91:
#     print('B')
# elif grade >= 71 and grade < 81:
#     print('C')
# elif grade >= 61 and grade < 71:
#     print('D')
# elif grade >= 51 and grade < 61:
#     print('E')
# elif grade < 51:
#     print('Kesildi')
# else:
#     print('0 və 100 arası ədəd daxil edin!')


if grade < 0:
    print('0 və 100 arası ədəd daxil edin!')
elif grade > 100:
    print('0 və 100 arası ədəd daxil edin!')
elif grade < 51:
    print('Kesildi')
elif grade < 61:
    print('E')
elif grade < 71:
    print('D')
elif grade < 81:
    print('C')
elif grade < 91:
    print('B')
elif grade <= 100:
    print('A')
else:
    print('Kesildi')
