# Tapşırıq 1:
# 1. Student adlı class yaradın.
# 2. Bu class-da ad, yaş və sinif atributları olsun.
# 3. Bir method yazın: introduce(), tələbə haqqında məlumat çap etsin.

# Nümunə nəticə:
# Salam, mənim adım Aysel-dir. Mən 17 yaşındayam və 11-ci sinifdə oxuyuram.


# Tapşırıq 2:
# 1. Calculator adlı class yaradın.
# 2. __init__ metodunda iki ədəd qəbul etsin.
# 3. Toplama, çıxma, vurma və bölmə metodlarını əlavə edin.

# Əlavə:
# Əgər bölünən 0 olarsa, "0-a bölmək olmaz!" mesajı qaytarsın.

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        ...

    def division(self):
        ...


c1 = Calculator(5, 15)
print(c1.addition())
print(c1.subtraction())


# Tapşırıq 3:
# 1. Rectangle adlı class yaradın.
# 2. Uzunluq və en atributları olsun.
# 3. area() və perimeter() metodları əlavə edin.

# Nümunə:
# area() -> uzunluq * en
# perimeter() -> 2 * (uzunluq + en)


# Tapşırıq 4:
# 1. Car adlı class yaradın.
# 2. Marka, model, il atributları olsun.
# 3. start(), stop() adlı metodlar əlavə edin.
# 4. start() işə düşdüyünü, stop() isə dayandığını bildirsin.


class Car:
    def __init__(self, marka, model, year):
        self.marka = marka
        self.model = model
        self.year = year

    def start(self):
        return 'Mühərrik işə düşdü!'

    def stop(self):
        return 'Mühərrik dayandı!'

c1 = Car('BMW', 'F30', 2015)
print(c1.start())
print(c1.stop())


# Tapşırıq 5:
# 1. Temperature adlı class yaradın.
# 2. Atribut: `celsius` (dərəcə).
# 3. Method: to_fahrenheit() → (°C × 9/5) + 32
# 4. Method: to_kelvin() → °C + 273.15


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius) * (9/5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15


t1 = Temperature(32)
print(t1.to_fahrenheit())
print(t1.to_kelvin())


# Tapşırıq 6:
# 1. Movie adlı class yaradın.
# 2. Adı, rejissoru və il atributları olsun.
# 3. info() metodu: "Inception (2010), directed by Christopher Nolan" qaytarsın.


class Movie:
    def __init__(self, name: str, producer: str, year: int):
        self.name = name.capitalize()
        self.producer = producer.title()
        self.year = year

    def info(self):
        return f"{self.name} ({self.year}), directed by {self.producer}"

m1 = Movie('inception', 'Christopher nolan', 2010)
print(m1.info())


# Tapşırıq 7:
# 1. Person, Developer, Designer classes təyin olunsun.
# 2. Hər bir sinifdə name, surname, age və maaş atributları olsun.
# 3. Developer class daxilində əlavə olaraq 
#   proqramçının bildiyi dil təyin olunsun.
# 4. Designer class daxilində əlavə olaraq 
#   dizaynerin bildiyi proqram təyin olunsun
