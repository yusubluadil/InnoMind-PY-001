# 1.​ İstifadəçinin daxil etdiyi cümlədə sözlərin ümumi sayını for loop
# istifadə edərək tapan proqram tərtib edin.


# sentence = input("Cümləni daxil edin: ").split()

# count = 0

# for _ in sentence:
#     count += 1

# print(count)



# 2.​ İstifadəçinin daxil etdiyi rəqəmlərin cəmini tapan proqram tərtib
# edin.

# num = input("Rəqəmləri daxil edin: ").strip()


# result = 0

# if num.isdigit():
#     for i in num:
#         result += int(i)

#     print(result)
# else:
#     print("Daxil edilən məlumat rəqəmlərdən ibarət deyil.")


# 3. İstifadəçinin daxil etdiyi rəqəmdə təkrar olunan elementləri
# göstərən proqram tərtib edin. (Məsələn, istifadəçi 125102 daxil
# edib. Bu zaman, [1, 2] print olunacaq. Çünki, təkrarlanan rəqəmlər
# 1 və 2-dir.)

num = input("Rəqəmləri daxil edin: ").strip()

result = []

for i in num:
    if num.count(i) > 1 and int(i) not in result:
        result.append(int(i))

print(result)
