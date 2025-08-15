# Abstraction and Encapsulation
# Property
# Classmethod
# Staticmethod



# Abstraction
# Zəruri metodların ön plana çıxarılmasıdır.

from abc import (
    ABC,
    abstractmethod
)

class Shape(ABC): # Abstract class
    @abstractmethod
    def area(self): # abstract method
        pass


class Circle(Shape):
    PI = 3.14

    def __init__(self, raidus: float):
        super().__init__()
        self.radius = raidus

    def area(self):
        return self.PI * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


c1 = Circle(20)
print(c1.area())


s1 = Rectangle(10, 20)
print(s1.area())


class Electronic(ABC):
    @abstractmethod
    def min_voltage(self):
        pass


class AirConditioner(Electronic):
    def min_voltage(self):
        return 220


class Computer(Electronic):
    def min_voltage(self):
        return 200


# Encapsulation (Kapsullamaq)
# Class daxilində olan metod və atributları gizlədilməsi
# və ya təhlükəsizliyinin təmin olunması

# Protected - Atribut və ya metod adının əvvəlində tək alt xətt ilə təyin olunur.
# Mesaj xarakteri daşıyır. Digər developerlər protected metod və ya atribut
# gördüyü zaman onları class-dan kənarda istifadə etməməyə çalışır.

# Private - Atribut və ya metod adının əvvəlində qoşa alt xətt ilə təyin olunur.
# Zəruri xarakter daşıyır. Private metod və ya atribut class-dan kənarda istifadə
# olunmağa çalışılarsa, xəta verərək proqram dayanır.

class BankAccount:
    def __init__(self, name, fin):
        self._name = name # Protected
        self.__fin = fin # Private
        self.__balance = 0 # Private

    def get_name(self):
        return self._name

    def get_fin(self):
        return self.__fin

    def set_fin(self, fin: str):
        self.__fin = fin.upper()


ba1 = BankAccount('Renad', '123456T')
# print(ba1._name) # Protected olduğu üçün class-dan kənarda istifadə edə bilərik.
# Amma tövsiyə olunmur. 

# print(ba1.__fin) # Private olduğu üçün xəta verəcək

print(ba1.get_name())
print(ba1.get_fin())

ba1.set_fin('123123a')

print(ba1.get_fin())



# Property - Method-un özünü atribut kimi aparması
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'


p1 = Person('Renad', 'Xasayev')

print(p1.fullname)


# Classmethod - Bununla təyin olunan metodlar ilk arqument olaraq class-ın özünü alır.
class Student:
    school_name = 'Signature Academy'

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name


st1 = Student('Renad')
st2 = Student('Aygün')

print(st1.school_name)
st1.change_school_name('InnoMind')
print(st1.school_name)

print(st2.school_name)

st3 = Student('Adil')
print(st3.school_name)


# Staticmethod - Nə class-ı, nə də ki, object-i arqument olaraq almır.
class Course:
    @staticmethod
    def welcome_message():
        return 'Xoş gəldiniz!'


c1 = Course()
print(c1.welcome_message())
