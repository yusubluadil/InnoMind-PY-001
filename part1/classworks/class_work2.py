# 1. İstifadəçi yaş daxil edir və həmin yaşa görə istifadəçinin
# uşaq, yeniyetmə, gənc, orta yaşlı və ya yaşlı olduğunu müəyyən edən proqram yazın.


age = int(input('Yaşınızı daxil edin: '))

if age <= 6:
    print('Uşaq')
elif age <= 18:
    print('Yeniyetmə')
elif age <= 30:
    print('Gənc')
elif age <= 50:
    print('Orta yaşlı')
elif age <= 70:
    print('Yaşlı')
else:
    print('Çox yaşlı')


# 2. İstifadəçinin daxil etdiyi ədədin müsbət, mənfi və ya sıfır olduğunu 
# müəyyən edən proqram yazın.

# 3. Tələbənin imtahan nəticəsini yoxlayan proqram yazın.
# (51-den kicik olarsa, kesilib. eks halda ise kecib)

# 4. İstifadəçidən 3 ədəd daxil etməsini istəyin. Bu 3 ədədin ən böyük olanını 
# müəyyən edən proqram yazın. # and == Arasdirmali task ==

# 5. 51-61 (E), 61-71 (D), 71-81 (C), 81-91 (B), 91-100 (A) qiymət sistemini
# tətbiq edən proqram yazın. (İstifadəçi balı daxil edəcək.)
