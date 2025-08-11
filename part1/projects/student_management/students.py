class Student:
    def __init__(self, sid: int, name: str, surname: str, age: int, grade: int):
        if not 1 <= grade <= 11:
            print('Sinif 1-11 aralığından seçilə bilər.')
        else:
            self.id = sid
            self.name = name
            self.surname = surname
            self.age = age
            self.grade = grade

    def __str__(self):
        return f"ID: {self.id} -> {self.name} {self.surname} ({self.grade})"


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, sid, name, surname, age, grade):
        student = Student(
            sid=sid,
            name=name,
            surname=surname,
            age=age,
            grade=grade
        )

        self.students.append(student)

        return student

    def remove_student(self, sid):
        student = self.find_student_by_id(sid)

        if student is not None:
            self.students.remove(student)
            print(f'{student.id} ID-li şagird müvəffəqiyyətlə silindi!')
        else:
            print('Şagird tapılmadı.')

    def list_students(self):
        if not self.students:
            print('Heç bir məlumat tapılmadı.')
        else:
            for student in self.students:
                print(student)

    def update_student(self, sid, name=None, surname=None, age=None, grade=None):
        student = self.find_student_by_id(sid)

        if student:
            student.name = name if name else student.name
            student.surname = surname if surname else student.surname
            student.age = int(age) if age else student.age
            student.grade = int(grade) if grade else student.grade

            print('Məlumatlar uğurla yeniləndi!')
        else:
            print('Şagird tapılmadı!')

    def find_student_by_id(self, sid):
        for student in self.students:
            if sid == student.id:
                return student

        return None
