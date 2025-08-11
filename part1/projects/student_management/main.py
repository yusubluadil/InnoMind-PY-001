from students import StudentManagementSystem


management = StudentManagementSystem()


while True:
    print("""
    1 -> Şagird əlavə et
    2 -> Bütün şagirdlərə bax
    3 -> Şagird məlumatlarını yenilə
    4 -> Şagird sil

    0 -> Proqramı sonlandır
""")

    operation = input('Əməliyyatı daxil edin: ')

    if operation == '1':
        sid = int(input('İD-ni daxil edin: '))
        name = input('Şagirdin adını daxil edin: ')
        surname = input('Şagirdin soyadını daxil edin: ')
        age = int(input('Şagirdin yaşını daxil edin: '))
        grade = int(input('Şagirdin sinfini daxil edin (1-11): '))

        st = management.add_student(
            sid=sid,
            name=name,
            surname=surname,
            age=age,
            grade=grade
        )

        print(st, 'müvəffəqiyyətlə əlavə edildi.')
    elif operation == '2':
        management.list_students()
    elif operation == '3':
        sid = int(input('İD-ni daxil edin: '))
        name = input('Şagirdin adını daxil edin (dəyişilməzsə, boş buraxın): ')
        surname = input('Şagirdin soyadını daxil edin (dəyişilməzsə, boş buraxın): ')
        age = input('Şagirdin yaşını daxil edin (dəyişilməzsə, boş buraxın): ')
        grade = input('Şagirdin sinfini daxil edin (1-11) (dəyişilməzsə, boş buraxın): ')

        management.update_student(
            sid=sid,
            name=name,
            surname=surname,
            age=age,
            grade=grade
        )
    elif operation == '4':
        sid = int(input('Şagirdin İD-ni daxil edin: '))

        management.remove_student(sid=sid)
    elif operation == '0':
        print('Proqram sonlandı...')
        break
    else:
        print('Yanlış əməliyyat daxil etdiniz.')
