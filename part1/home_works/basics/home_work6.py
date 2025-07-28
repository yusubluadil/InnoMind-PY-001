# 1.​ İki hərf daxil edilir və əlifbaya görə hansı ilk olaraq gəlməlidirsə, o göstərilir.


letter1 = input("Birinci hərfi daxil edin: ")
letter2 = input("İkinci hərfi daxil edin: ")

# letters = sorted([letter1, letter2])
letters = [letter1, letter2]
letters.sort()

print(letters[0])



# 2.​ Telefon PİN yoxlayıcı. Doğru PİN “5432” şəklindədir və istifadəçi 3
# cəhdə doğru pini daxil etməzsə, bu zaman bloklanması barədə
# mesaj verilsin.


pin = "5432"

input_pin1 = input("PİN kodu daxil edin: ")
if input_pin1 == pin:
    print("PİN kod doğrudur.")
else:
    print("PİN kod yanlışdır. Yenidən cəhd edin.")

    input_pin2 = input("PİN kodu daxil edin (2-ci cəhd): ")
    if input_pin2 == pin:
        print("PİN kod doğrudur.")
    else:
        print("PİN kod yanlışdır. Yenidən cəhd edin.")

        input_pin3 = input("PİN kodu daxil edin (3-cü cəhd): ")
        if input_pin3 == pin:
            print("PİN kod doğrudur.")
        else:
            print("Siz bloklandınız. PİN kod 3 dəfə yanlış daxil edilmişdir!")



# 3.​ İstifadəçi 1-7 aralığında hər hansısa bir ədəd daxil edəcək. Daxil
# edilən ədədin hansı gün olduğunu təyin edən proqram yazın.
# Məsələn, 7 daxil edilərsə, Bazar günü çap olunacaq.

day_num = int(input("1-7 aralığında bir ədəd daxil edin: "))


if day_num == 1:
    print("Bazar ertəsi")
elif day_num == 2:
    print("Çərşənbə axşamı")
elif day_num == 3:
    print("Çərşənbə")
elif day_num == 4:
    print("Cümə axşamı")
elif day_num == 5:
    print("Cümə")
elif day_num == 6:
    print("Şənbə")
elif day_num == 7:
    print("Bazar")
else:
    print("Daxil edilən ədəd 1-7 aralığında deyil. Zəhmət olmasa, düzgün ədəd daxil edin.")



# 4.​ İstifadəçi məbləğ daxil edir. Əgər məbləğ 100 AZN-dən böyük
# olarsa, daxil edilən məbləğə 15% endirim tətbiq olunacaq, əks
# halda isə heç bir endirim tətbiq olunmur.


amount = float(input("Məbləği daxil edin (AZN): "))

if amount >= 100:
    amount = amount * 0.85
    print(f"Endirimli məbləğ: {amount:.2f} AZN")
else:
    print(f"Endirim tətbiq olunmadı. Daxil edilən məbləğ: {amount:.2f} AZN")



# 5.​ Elektrik sərfiyyatı (kWh) daxil edilsin. İlk 150 kWh: 0.07 AZN/kWh.
# Sonrakı hər kWh: 0.11 AZN. İstifadəçi sərfiyyatı daxil edəcək və
# ona uyğun məbləğ hesablanıb istifadəçiyə təqdim olunacaq.

consumption = float(input("Elektrik sərfiyyatını (kWh) daxil edin: "))

if consumption <= 150:
    total = consumption * 0.07
else:
    total = (150 * 0.07) + ((consumption - 150) * 0.11)

print(f"Ümumi məbləğ: {total:.2f} AZN")



# 6.​ Bank kredit kalkulyatoru. İstifadəçi öz maaşını, əldə etmək istədiyi
# məbləği və ayı daxil edir. Aylıq ödəniş məbləği maaşın 40%-dən
# aşağı olarsa, bu zaman krediti əldə edə bilər. Əks halda isə Kredit
# götürə bilməz.

salary = float(input("Maaşınızı daxil edin (AZN): "))
wanted_amount = float(input("Əldə etmək istədiyiniz məbləği daxil edin (AZN): "))
months = int(input("Kredit müddətini aylarla daxil edin: "))

payment_amount = wanted_amount / months


if payment_amount <= (salary * 0.4):
    print(f"Krediti əldə edə bilərsiniz. Aylıq ödəniş məbləği: {payment_amount:.2f} AZN")
else:
    print("Kredit götürə bilməzsiniz. Aylıq ödəniş məbləği maaşınızın 40%-dən çoxdur.")
