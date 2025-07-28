# Bank ATM sistemi tərtib edin.

# İstifadəçi 0 daxil edənə kimi proqram davam edəcək.
# İstifadəçi sanki kartı və kodu daxil edəcək.
# Əgər kart və şifrə məlumatları doğru olarsa, sistem açılacaq.
# Sistem açıldıqdan sonra, 
#       Balansa, baxmaq üçün 1 daxil edəcək
#       Məbləğ əlavə etmək üçün 2 daxil edəcək
#       Məbləğ xaric etmək üçün 3 daxil edəcək


DB = {
    '5539 2328 4565 1245': {'password': '2002', 'balance': 2000},
    '5539 2328 4565 7456': {'password': '1001', 'balance': 800},
    '5539 2328 7452 1245': {'password': '0000', 'balance': 145}
}


while True:
    card_number = input('Kartı daxil edin (və ya çıxış üçün 0 daxil edin.): ')

    if card_number == '0':
        print('Əməliyyat sonlandı...')
        break
    else:
        if card_number in DB.keys():
            password = input('PİN-i daxil edin: ')
            if password == DB[card_number]['password']:
                print("""
                    1 --> Balansı göstər;
                    2 --> Mədaxil et;
                    3 --> Məxaric et;
                    0 --> Sonlandır.
                """)

                operation = int(input("Əməliyyatı daxil edin: "))
                if operation == 1:
                    balance = DB[card_number]['balance']
                    print(f"Sizin balansınız {balance} AZN-dir!")
                elif operation == 2:
                    amount = int(input('Mədaxil olunacaq məbləği daxil edin: '))
                    DB[card_number]['balance'] += amount
                    print(f'{amount} AZN məbləğ mədaxil olundu!')
                    print(f"Hazırkı balansınız {DB[card_number]['balance']} AZN-dir!")
                elif operation == 3:
                    amount = int(input('Məxaric olunacaq məbləği daxil edin: '))
                    if DB[card_number]['balance'] < amount:
                        print(f"Kifayət qədər məbləğ balansınızda mövcud deyil! Sizin balansınız {DB[card_number]['balance']} AZN-dir!")
                    else:
                        DB[card_number]['balance'] -= amount
                        print(f'{amount} AZN məbləğ məxaric olundu!')
                        print(f"Hazırkı balansınız {DB[card_number]['balance']} AZN-dir!")
                elif operation == 0:
                    print('Əməliyyat sonlandı...')
                    break
                else:
                    print('Yanlış əməliyyat!')
            else:
                print('PİN yanlışdır!')
        else:
            print('Kart nömrəsi yanlışdır!')
