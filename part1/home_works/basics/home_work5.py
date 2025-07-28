# 1.​ Daxil edilən ayın neçə gün çəkdiyini göstərən proqram yazın.
# Məsələn, istifadəçi yanvar daxil edirsə, o zaman 31 gün çap
# olunacaq.

# month = input("Ayın adını daxil edin: ").lower()

# months31 = ['yanvar', 'mart', 'may', 'iyul', 'avqust', 'oktyabr', 'dekabr']
# months30 = ['aprel', 'iyun', 'sentyabr', 'noyabr']
# months28_29 = ['fevral']

# if month in months31:
#     print(f"{month.capitalize()} ayı 31 gün çəkir.")
# elif month in months30:
#     print(f"{month.capitalize()} ayı 30 gün çəkir.")
# elif month in months28_29:
#     print(f"{month.capitalize()} ayı 28 və ya 29 gün çəkir.")
# else:
#     print('Daxil edilən ay düzgün deyil!')


# 2.​ Daxil edilən hərfin sait və ya samit olduğunu yoxlayan proqram
# tərtib edin.

# letter = input("Bir hərf daxil edin: ").lower()

# # vowels = ['a', 'e', 'i', 'o', 'u', 'ü', 'ö', 'ə', 'ı']
# vowels = 'aıoueəiöü'

# if letter in vowels:
#     print(f"{letter} sait hərfdir.")
# else:
#     print(f"{letter} samit hərfdir.")



# 3.​ Daxil edilən parolun güclü və ya zəif olduğunu yoxlayan proqram
# tərtib edin. Güclü parol olması üçün simvol sayı 8-dən çox
# olmalıdır. Məsələn, adil123 zəif paroldur.

# pswd = input("Parolu daxil edin: ")

# if len(pswd) >= 8:
#     print("Güclü parol!")
# else:
#     print("Zəif parol! Parolun uzunluğu 8 simvoldan azdır.")


# 4.​ İstifadəçi iki ədəd və riyazi əməliyyatı daxil edəcək. Buna uyğun da
# hesablama aparan proqram tərtib edin. Məsələn, 4 sonra isə 2
# daxil edilir və daha sonra isə / daxil edilir. Bu zaman 4 2-yə bölünür
# və nəticə çap olunur.

num1 = float(input("Birinci ədədi daxil edin: "))
num2 = float(input("İkinci ədədi daxil edin: "))

print(
    "% -> Bölmədən alınan qalıq\n",
    "// -> Bölmədən alınan tam hissə\n",
    "** -> Qüvvəti\n"
)

operation = input("Riyazi əməliyyatı daxil edin (+, -, *, /, %, //, **): ")


if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    if num2 == 0:
        print("Sıfıra bölmək mümkün deyil!")
    else:
        print(num1 / num2)
elif operation == '%':
    if num2 == 0:
        print("Sıfıra bölmək mümkün deyil!")
    else:
        print(num1 % num2)
elif operation == '//':
    if num2 == 0:
        print("Sıfıra bölmək mümkün deyil!")
    else:
        print(num1 // num2)
elif operation == '**':
    print(num1 ** num2)
else:
    print("Daxil edilən əməliyyat düzgün deyil!")
