import random

# 1. 1-dən 100-ə qədər 3-ə bölünən ədədləri çap et

# 2. 0-dan 50-yə qədər cüt ədədləri while dövrü ilə çap et

# 3. 1-dən 100-ə qədər ədədlərdən həm 3-ə, həm 5-ə bölünənləri çap et
    # Ancaq "FizzBuzz" kimi:
    #     3-ə bölünürsə → "Fizz"
    #     5-ə bölünürsə → "Buzz"
    #     Hər ikisinə bölünürsə → "FizzBuzz"
    #     Yoxsa ədədin özünü çap et.

# 4. İstifadəçidən mətni al və hər bir sözün uzunluğunu çap et
# Giriş: "Salam dünya bu testdir"
# Çıxış: Salam - 5, dünya - 5, bu - 2, testdir - 7

# 5. Ədəddəki ən böyük rəqəmi tap
# Məsələn: 98352 → 9

number = '132352'

max_value = 0
for i in number:
    if int(i) > max_value:
        max_value = int(i)
print(max_value)

# 6. Bir mətndə neçə ədəd olduğunu tap
# Giriş: "Bu gün 3 qələm, 2 kitab və 1 çanta aldım."
# Çıxış: 3 ədəd rəqəm tapıldı: 3, 2, 1

def get_num_count(string: str):
    numbers = []
    for i in string:
        if i.isdigit():
            numbers.append(int(i))

    print(f'{len(numbers)} ədəd rəqəm tapıldı:', end=' ')
    for num in numbers:
        print(num, end=', ')
    else:
        print('\n')

get_num_count('Bu gün 3 qələm, 2 kitab və 1 çanta aldım.')

# 7. Təkrarlanan hərfləri say
# Giriş: "programming"
# Çıxış: {'r': 2, 'g': 2, 'm': 2}

# 8. Tərs üçbucaq çap et
# Giriş: 5
# Çıxış:
"""
*****
****
***
**
*
"""

# 9. Binary çevirici: ədəd al və 2-lik say sisteminə dövr ilə çevir

# num = 24
# reversed_binary_num = ''
# while num > 1:
#     residue = str(num % 2)
#     num = num // 2

#     reversed_binary_num += residue
# reversed_binary_num += str(num)

# print(reversed_binary_num[::-1])

# 10. Pythonda ədədləri piramida şəklində çap et
# Giriş: 5
# Çıxış:
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

# 11. Ədədi bölənlərini tap
# Məsələn: 12 → [1, 2, 3, 4, 6, 12]

number = 12
dividers = []
for i in range(1, number + 1):
    if number % i == 0:
        dividers.append(i)

print(number, dividers, sep=' → ')

# 12. Hər dəfə sonuncu hərfi çıxararaq çap et:
# Çıxış:
"""
salam
sala
sal
sa
s
"""

# 13. Ədədi rəqəmlərinə görə artan sıraya sal
# 329 → 239

# 14. Mətndəki bütün sözləri tərsinə yaz, cümlənin öz strukturunu saxla
# Giriş: "Salam dünya"
# Çıxış: "malaS aynyüd"

txt = "Salam dünya"
splitted_txt = txt.split()
result = ''

for i in splitted_txt:
    result += i[::-1]
    result += ' '

print(result)

# 15. "Təxmin oyunu"
#     Kompüter 1-dən 20-yə qədər bir ədəd seçir.
#     İstifadəçi təxmin edir, proqram deyir: "artır", "azalt" və ya "doğrudur".
#     Ən sonda proqram neçə cəhddə ədədi tapdığımızı qaytarsın.
#     while dövrü ilə qur.

num = random.randrange(1, 21) # 15
entered_num = None
counter = 1

while entered_num != num:
    try:
        entered_num = int(input("bir ədəd daxil edin: "))
    except:
        print('Ədəd daxil edin')
        continue

    if entered_num > num:
        print("Azalt!")
    elif entered_num < num:
        print('Artır!')
    else:
        print(f'Təbriklər siz ədədi {counter} cəhddə tapdız.')

    counter += 1
