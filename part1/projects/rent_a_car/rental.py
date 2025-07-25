from db import DB


def rent_car(license_plate: str) -> dict:
    op_car = None
    for car in DB:
        if car.get('license_plate') == license_plate:
            if not car.get('is_avaliable'):
                print(f'{license_plate} qeydiyyat nişanlı avtomobil icarədədir.')
                return

            car['is_avaliable'] = False
            op_car = car

    if op_car is not None:
        print(f'{license_plate} qeydiyyat nişanlı avtomobil icarəyə verildi.')
    else:
        print('Avtomobil tapılmadı!')


def return_car(license_plate: str) -> dict:
    op_car = None
    for car in DB:
        if car.get('license_plate') == license_plate:
            if car.get('is_avaliable'):
                print(f'{license_plate} qeydiyyat nişanlı avtomobil salondadır.')
                return

            car['is_avaliable'] = True
            op_car = car

    if op_car is not None:
        print(f'{license_plate} qeydiyyat nişanlı avtomobil geri alındı.')
    else:
        print('Avtomobil tapılmadı!')
