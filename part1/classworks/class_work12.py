# Task1: Kredit Kartı Nömrəsinin Yoxlanması
# İstifadəçi kredit kartı nömrəsini daxil edir və funksiya bu nömrənin düzgünlüyünü yoxlayır.

# 1. Kart nömrəsi 16 rəqəmdən ibarət olmalıdır (və ya 4-dən birində - simvolu ola bilər, məsələn: 1234-5678-9012-3456).
# 2. Yalnız rəqəmlər və tire işarələri (-) istifadə oluna bilər.
# 3. Əgər tire (-) istifadə olunubsa, onlar dəqiq 4 yerə bölünməli və 4 ədəd 4 rəqəmli hissə olmalıdır.
# 4. Kart nömrəsi 4, 5 və ya 6 ilə başlamalıdır.
# 5. Eyni rəqəm 4 və ya daha çox dəfə təkrarlanarsa, kart nömrəsi etibarsız sayılır (məsələn: 1111222233334444 - etibarsızdır).

# 4169738856564543
# 4169-7388-5656-4543

card = '4169738856564543'
card2 = '4169-7388-5656-4543'

print(card.split('-'))
print(card2.split('-'))





# Task2: E-mail Ünvanlarının Yoxlanması və Filtrlənməsi
# İsifadəçinin daxil etdiyi e-mail ünvanını funksiya yazın.

# 1. username@websitename.extension formatında olmalıdır.
# 2. username yalnız hərflər (a–z, A–Z), rəqəmlər (0–9), alt xətt (_), tire (-), nöqtə (.) simvollarını ehtiva edə bilər.
# 3. websitename yalnız hərflər və rəqəmlərdən ibarət ola bilər.
# 4. extension maksimum 3 hərfdən ibarət olmalıdır.
