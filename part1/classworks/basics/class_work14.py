# Daş, kağız və qayçı oyunu

import random

choices_list = ['Daş', 'Kağız', 'Qayçı']
print('Oyunu sonlandırmaq üçün 0 daxil edin.')

while True:
    comp_choice = random.choice(choices_list)
    user_choice = input('Seçiminizi daxil edin: ').capitalize()
    if user_choice == '0':
        print('Oyun sonlandı...')
        break

    if user_choice in choices_list:
        if comp_choice == 'Daş':
            if user_choice == 'Kağız':
                print('User qazandı')
            elif user_choice == 'Qayçı':
                print('Komputer qazandı')
            else:
                print('Heç-heçə')
        elif comp_choice == 'Kağız':
            if user_choice == 'Kağız':
                print('Heç-heçə')
            elif user_choice == 'Qayçı':
                print('User qazandı')
            else:
                print('Komputer qazandı')
        else:
            if user_choice == 'Kağız':
                print('Komputer qazandı')
            elif user_choice == 'Qayçı':
                print('Heç-heçə')
            else:
                print('User qazandı')
    else:
        print('Düzgün daxil edin!')
