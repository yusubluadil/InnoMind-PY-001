from car import (
    create_car,
    list_cars,
    update_car,
    delete_car
)

from rental import (
    rent_car,
    return_car
)

from log import create_log


while True:
    print("""
    1 -> Avtomobil əlavə et
    2 -> Bütün avtomobillərə bax
    3 -> Avtomobil məlumatlarını yenilə
    4 -> Avtomobil sil
    5 -> Avtomobili icarəyə ver
    6 -> Avtomobili geri götür
    0 -> Proqramı sonlandır
""")

    operation = input('Əməliyyatı daxil edin: ')

    if operation == '1':
        brand = input('Avtomobil markasını daxil edin: ')
        model = input('Avtomobil modelini daxil edin: ')
        year = int(input('Avtomobilin buraxılış ilini daxil edin: '))
        license_plate = input('Avtomobilin qeydiyyat nişanını daxil edin: ')
        daily_price = float(input('Avtomobilin günlük icarə qiyməti: '))
        is_avaliable = True

        car = create_car(
            brand=brand,
            model=model,
            year=year,
            license_plate=license_plate,
            daily_price=daily_price,
            is_avaliable=is_avaliable
        )

        print(f'{license_plate} nömrəli avtomobil sistemə əlavə olundu.')
        create_log('1', license_plate=license_plate)
    elif operation == '2':
        list_cars()
        create_log('2')
    elif operation == '3':
        license_plate = input("Avtomobil qeydiyyat nişanını daxil edin: ")

        updated_car = update_car(license_plate)
        if updated_car != {}:
            print(updated_car)
            print('Məlumatlar uğurla yeniləndi!')
        create_log('3', license_plate=license_plate)
    elif operation == '4':
        license_plate = input("Avtomobil qeydiyyat nişanını daxil edin: ")

        delete_car(license_plate)
        create_log('4', license_plate=license_plate)
    elif operation == '5':
        license_plate = input("Avtomobil qeydiyyat nişanını daxil edin: ")

        rent_car(license_plate)
        create_log('5', license_plate=license_plate)
    elif operation == '6':
        license_plate = input("Avtomobil qeydiyyat nişanını daxil edin: ")

        return_car(license_plate)
        create_log('6', license_plate=license_plate)
    elif operation == '0':
        print('Proqram sonlandı...')
        create_log('0')
        break
    else:
        print('Daxil edilən əməliyyat sistemdə mövcud deyil!')
        create_log()
