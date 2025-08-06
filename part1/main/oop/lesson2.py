# class attributes
# Dunder methods (double underscore methods və ya magic methods)
# __init__, __str__, __len__, __add__, __eq__, etc.
# Method Overriding
# Polymorphism


# class Car:
#     wheels = 4 # class attribute

#     def __init__(self, marka, model):
#         self.marka = marka
#         self.model = model

# c1 = Car('Toyota', 'Corolla')
# print(c1.wheels)

# c2 = Car('Ford', 'Fusion')
# print(c2.wheels)

# Car.wheels = 5
# # c1.wheels = 5
# c1.marka = 'Lexus'

# print(c1.marka)
# print(c1.wheels)
# print(c2.wheels)



# Dunder methods (double underscore methods və ya magic methods)
# __init__, __str__, __len__, __add__, __eq__, etc.

# class Book:
#     def __init__(self, name: str, pages_count: int):
#         self.name = name
#         self.pages_count = pages_count

#     def __str__(self):
#         return f"{self.name}, {self.pages_count}"

#     def __len__(self):
#         return self.pages_count

#     def __add__(self, other):
#         return self.pages_count + other.pages_count

#     def __eq__(self, other):
#         return self.pages_count == other.pages_count


# book1 = Book('Python', 300)
# book2 = Book('Django', 300)

# print(book1)
# print(len(book1))
# print(book1 + book2)
# print(book1 == book2)


# Method Overriding
# Polymorphism - Çox şaxəlilik (Eyni adlı metodların fərqli nəticələr göstərməsi)

class Animal:
    def speak(self):
        return 'Hər hansısa bir səs'


class Dog(Animal):
    def speak(self):
        return 'İt hürür.'


class Cat(Animal):
    def speak(self):
        return 'Pişik miyoldayır.'


d1 = Dog()
c1 = Cat()

print(d1.speak())
print(c1.speak())
