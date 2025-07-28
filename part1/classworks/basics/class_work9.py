"""

Sezar Şifrələməsi: Tarixi və İstifadə Sahələri

Tarixi:
    Sezar şifrələməsi adını Roma imperatoru Yuli Sezardan alıb.
    Sezar bu üsulu ordularına göndərdiyi gizli məktublarda istifadə edirdi.
    Məqsəd mesajların düşmən tərəfindən oxunmasının qarşısını almaq idi.

    O, mesajdakı hərfləri əlifbada müəyyən sayda sürüşdürərək şifrələyirdi.
    Məsələn, "A" hərfini 3 hərf sağa sürüşdürüb "C" edirdi.

İstifadə Yeri:
    Bu üsul əvvəllər hərbi yazışmalarda istifadə edilib.
    Kriptoqrafiya öyrənmək üçün təməl nümunə kimi;
    Məktəblərdə və proqramlaşdırma dərslərində məşq məqsədilə;
    Sadə oyunlar və tətbiqlərdə.

"""


# 1. Daxil edilmiş mətni Sezar şifrələməsi ilə şifrələyən proqram tərtib edin.
# 2. Sezar şifrələməsi ilə şifrələnmiş mətni açan proqram tərtib edin.


AZ_ALPHABET_UPPER = "ABCÇDEƏFGĞHXIİJKQLMNOÖPRSŞTUÜVYZ"
AZ_ALPHABET_LOWER = "abcçdeəfgğhxıijkqlmnoöprsştuüvyz"


txt = input('Mətni daxil edin: ')
c = int(input('Şifrələmə üçün rəqəmi daxil edin: '))
result = ''


# print((0 + 3 - 1) % 32) # 2
# print((30 + 3 - 1) % 32) # 0


if 2 <= c <= 32:
    for i in txt:
        if i in AZ_ALPHABET_UPPER:
            index = (AZ_ALPHABET_UPPER.index(i) + c - 1) % len(AZ_ALPHABET_UPPER)
            result += AZ_ALPHABET_UPPER[index]
        elif i in AZ_ALPHABET_LOWER:
            index = (AZ_ALPHABET_LOWER.index(i) + c - 1) % len(AZ_ALPHABET_LOWER)
            result += AZ_ALPHABET_LOWER[index]
        else:
            result += i
else:
    print('Daxil edilən ədəd 2-32 aralığında olmalıdır.')

print(result)
