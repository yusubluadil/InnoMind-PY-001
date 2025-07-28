# 1.​ “Mən python öyrənirəm!” stringini tərs çap edən proqram yazın.

# Stringlerin indexi var!

text = "Mən python öyrənirəm!"

print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])

# # 'M' + 'ə' + 'n'
# print(text[0] + text[1] + text[2]) # İşləyir, amma uzun çəkir

# print(text[0+1+2]) # Bu cur yazilis text[3] ile eynidir


# text[start:end]
print(text[0:2]) # Son index daxil deyil (Mə)
print(text[0:3]) # (Mən)

print(text[:3]) # 0-dan 3-ə qədər olan hissə


print(text[0:10:2]) # 0-dan 10-a qədər olan hissə, 2 addım ilə
print(text[0:10:3]) # 0-dan 10-a qədər olan hissə, 3 addım ilə


print(text[-1]) # Sonuncu simvol
print(text[-2])

# Tərs çevirir
print(text[::-1]) # !mərinəryö nohtyp nəM


# 2.​ İstifadəçidən ad və soyadı alan proqram yazın.
# name = input("Adınızı daxil edin: ")
# surname = input("Soyadınızı daxil edin: ")
# age = input('Yaşınızı daxil edin: ')

# print(name + ' ' + surname + ' ' + age + ' yaşım var.')


# 3.​ İstifadəçinin daxil etdiyi 2 ədədi toplayan proqram yazın.

# print('Adil', 'Yusublu', '22', 'yas', 55)
# input() - default olaraq str verir.

num1 = int(input('Birinci ədədi daxil edin: '))
num2 = int(input('Ikinci ədədi daxil edin: '))
total = num1 + num2

print('Cəm:', total)

# 4.​ İstifadəçinin daxil etdiyi 2 ədədi bölən proqram yazın.
num1 = int(input('Birinci ədədi daxil edin: '))
num2 = int(input('Ikinci ədədi daxil edin: '))
fate = num1 / num2

print('Qismət:', fate)
