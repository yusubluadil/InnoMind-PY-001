from datetime import datetime


def create_log(operation, **kwargs):
    now = datetime.now()

    if operation == '1':
        log_data = f"[{now}] INFO: 'admin' {kwargs.get('license_plate')} qeydiyyat nişanlı avtomobili sistemə `əlavə etdi`.\n"
    elif operation == '2':
        log_data = f"[{now}] INFO: 'admin' bütün avtomobillərə `baxdı`.\n"
    elif operation == '3':
        log_data = f"[{now}] INFO: 'admin' {kwargs.get('license_plate')} qeydiyyat nişanlı avtomobil `məlumatlarını yenilədi`.\n"
    elif operation == '4':
        log_data = f"[{now}] INFO: 'admin' {kwargs.get('license_plate')} qeydiyyat nişanlı avtomobili sistemdən `sildi`.\n"
    elif operation == '5':
        log_data = f"[{now}] INFO: 'admin' {kwargs.get('license_plate')} qeydiyyat nişanlı avtomobili `icarəyə verdi`.\n"
    elif operation == '6':
        log_data = f"[{now}] INFO: 'admin' {kwargs.get('license_plate')} qeydiyyat nişanlı avtomobili `geri aldı`.\n"
    elif operation == '0':
        log_data = f"[{now}] INFO: 'admin' `proqramı sonlandırdı`.\n"
    else:
        log_data = f"[{now}] INFO: 'admin' mövcud olmayan əməliyyatı icra etməyə çalışdı.\n"

    with open('part1/projects/rent_a_car/logs/activity.log', mode='a', encoding='utf-8') as file:
        file.write(log_data)
