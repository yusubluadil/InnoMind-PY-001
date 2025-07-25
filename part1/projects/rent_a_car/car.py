from db import DB


def create_car(
    *,
    brand: str,
    model: str,
    year: int,
    license_plate: str,
    daily_price: float,
    is_avaliable: bool
) -> dict:
    car_data = {
        "brand": brand,
        "model": model,
        "year": year,
        "license_plate": license_plate,
        "daily_price": daily_price,
        "is_avaliable": is_avaliable
    }

    DB.append(car_data)

    return car_data


def list_cars():
    if len(DB) == 0:
        print('Heç bir məlumat tapılmadı.')
    else:
        for car in DB:
            print(car)


def update_car(license_plate: str) -> dict:
    op_car = None
    for car in DB:
        if car.get('license_plate') == license_plate:
            op_car = car
            DB.remove(car)
            break

    if op_car is not None:
        brand = input('Avtomobil markasını daxil edin: ')
        model = input('Avtomobil modelini daxil edin: ')
        year = int(input('Avtomobilin buraxılış ilini daxil edin: '))
        license_plate = input('Avtomobilin qeydiyyat nişanını daxil edin: ')
        daily_price = float(input('Avtomobilin günlük icarə qiyməti: '))

        op_car['brand'] = brand
        op_car['model'] = model
        op_car['year'] = year
        op_car['license_plate'] = license_plate
        op_car['daily_price'] = daily_price

        DB.append(op_car)
        return op_car
    else:
        print('Daxil edilən qeydiyyat nişanına uyğun məlumat tapılmadı!')
        return {}


def delete_car(license_plate: str) -> None:
    del_car = None
    for car in DB:
        if car.get('license_plate') == license_plate:
            del_car = car
            DB.remove(car)

    if del_car is not None:
        print(f'{license_plate} qeydiyyat nişanlı avtomobil silindi!')
    else:
        print('Avtomobil mövcud deyil!')
