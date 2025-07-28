from datetime import datetime
# OOP - Object Oriented Programming (Obyekt Yönümlü Proqramlaşdırma)

# num1 = int('40')
# print(type(num1), num1)

# str_num = str(55)
# print(type(str_num), str_num)

# list, dict, tuple, set, complex, float


# class, objects, attributes and methods(functions)

class Fruit: # class
    def __init__(self, name, color, taste): # method or function or constructor
        # Obyekt yaradılan zaman ilk işə düşən func budur.
        # self - obyektin özünü təmsil edir.

        self.name = name
        self.color = color
        self.taste = taste

fruit1 = Fruit('alma', 'qırmızı', 'şirin') # object

print(type(fruit1))
print(fruit1.name)
print(fruit1.color)
print(fruit1.taste)


class Person:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.age = age

    def birth_year(self): # Method və ilk arqument obyektin özü
        return datetime.now().year - self.age

    def get_fullname(self):
        return self.name + ' ' + self.surname


p1 = Person('Aygün', 'Ağazadə', 20)
p2 = Person('Renad', 'Xasayev', 42)
p3 = Person('Adil', 'Yusublu', 22)

print(p1.birth_year())
print(p2.birth_year())
print(p3.birth_year())

print(p1.get_fullname())


# class WorkerType:
#     ...

# class ContractModel:
#     ...



# OOP-nin 4 əsas prinsipi var.
# Inheritance, Encapsulation, Polymorphism and Abstraction

# Inheritance - Miras almaq

class Electronic:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def get_info(self):
        return f'{self.brand} - {self.color}'


class Computer(Electronic):
    def __init__(self, brand, color, ram, rom, rom_useage):
        super().__init__(brand, color)
        self.ram = ram
        self.rom = rom
        self.rom_useage = rom_useage

    def get_info(self):
        return f'{self.brand} - {self.color} - {self.ram}GB - {self.rom}GB - {self.rom_useage}GB'

    def get_free_place(self):
        return self.rom - self.rom_useage


class Phone(Electronic):
    ...


c1 = Computer('HP', 'Boz', 16, 512, 86)
phone = Phone('Apple', 'Mavi')

print(c1.brand)
print(c1.rom, c1.ram)

print(c1.get_info())
print(c1.get_free_place())
print(phone.get_info())
