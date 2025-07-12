# Task1: Kredit Kartı Nömrəsinin Yoxlanması
# İstifadəçi kredit kartı nömrəsini daxil edir və funksiya bu nömrənin düzgünlüyünü yoxlayır.

# 1. Kart nömrəsi 16 rəqəmdən ibarət olmalıdır (və ya 4-dən birində - simvolu ola bilər, məsələn: 1234-5678-9012-3456).
# 2. Yalnız rəqəmlər və tire işarələri (-) istifadə oluna bilər.
# 3. Əgər tire (-) istifadə olunubsa, onlar dəqiq 4 yerə bölünməli və 4 ədəd 4 rəqəmli hissə olmalıdır.
# 4. Kart nömrəsi 4, 5 və ya 6 ilə başlamalıdır.
# 5. Eyni rəqəm 4 və ya daha çox dəfə təkrarlanarsa, kart nömrəsi etibarsız sayılır (məsələn: 1111222233334444 - etibarsızdır).


def is_valid_card(card_number: str=None) -> bool:
    if card_number is not None:
        if card_number[0] == '4' or card_number[0] == '5' or card_number[0] == '6':
            if len(card_number) == 16:
                for num in card_number:
                    if card_number.count(num) >= 4:
                        return False
                return True
            elif len(card_number) == 19:
                splitted_numbers = card_number.split('-')
                new_card_number = ''.join(splitted_numbers)

                for num in new_card_number:
                    if new_card_number.count(num) >= 4:
                        return False
                return True
            else:
                return False
        else:
            return False
    else:
        return False


cards = ['4169738856564543', '5169-7388-5656-4543', '5169-7388-9656-4543']

for card in cards:
    if is_valid_card(card):
        print("Kart məlumatları doğrudur.")
    else:
        print("Kart məlumatları yanlışdır.")



# Task2: E-mail Ünvanlarının Yoxlanması
# İsifadəçinin daxil etdiyi e-mail ünvanını yoxlayan funksiya yazın.

# 1. username@websitename.extension formatında olmalıdır.
# 2. username yalnız hərflər (a–z, A–Z), rəqəmlər (0–9), alt xətt (_), tire (-), nöqtə (.) simvollarını ehtiva edə bilər.
# 3. websitename yalnız hərflər və rəqəmlərdən ibarət ola bilər.
# 4. extension maksimum 3 hərfdən ibarət olmalıdır.
import string

valid_symbols = string.ascii_letters + string.digits + '_' + '-' + '.'


def is_valid_email(email: str=None) -> bool:
    username, web_ext = email.split('@')

    for symbol in username:
        if symbol not in valid_symbols:
            return False

    webname, ext = web_ext.split('.')

    if not webname.isalnum():
        return False

    if not ext.isalpha() or len(ext) > 3:
        return False

    return True


emails = ['yusubluadil00@gmail.com', 'python#@gmail.com', 'adil_444@inno.azer']

for email in emails:
    if is_valid_email(email):
        print('Daxil edilən email doğrudur!')
    else:
        print('Daxil edilən email yanlışdır!')
