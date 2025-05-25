# 1. İstifadəçi məbləği (manat) və valyutanı ('euro', 'rub', 'usd') daxil edir.
# Daxil edilən məbləğ daxil edilmiş valyutaya çevirən proqram qurun.

# =============================================================== #
#                           euro = 2.0                            #
#                           rub = 0.018                           #
#                           usd = 1.7                             #
# =============================================================== #

amount = float(input("Məbləği daxil edin (manat): "))
currency = input("Valyutanı daxil edin (euro, rub, usd): ").lower()

currencies = ['euro', 'rub', 'usd']


if currency in currencies:
    if currency == 'euro':
        rounded_amount = round(amount / 2.0, 2)
        print(f"{rounded_amount} Euro")
    elif currency == 'rub':
        rounded_amount = round(amount / 0.018, 2)
        print(f"{rounded_amount} Rub")
    else:
        rounded_amount = round(amount / 1.7, 2)
        print(f"{rounded_amount} USD")
else:
    print("Daxil edilən valyuta uyğun deyil!")



# 2. Istifadəçinin daxil etdiyi avtomobil sürətinə görə cərimə
# tətbiq edən proqram yazın. (60-lıq yol)
# =============================================================== #
#                     70 - 80 km/s -> 10 manat                    #
#                     91 - 100 km/s -> 50 manat                   #
#                     101 - 120 km/s -> 150 manat                 #
#                     121 >= -> 15 günlük həbs                    #
# =============================================================== #
