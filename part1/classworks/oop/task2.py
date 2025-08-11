"""

BankAccount Class
BankAccount adlı bir class yaradın.

Bu class aşağıdakı atributlara sahib olsun:
    owner (hesab sahibi)
    balance (balans, default olaraq 0)

Aşağıdakı metodları yazın:
    deposit(amount) - hesaba pul əlavə etsin.
    withdraw(amount) - hesabdan pul çıxartsın.
    check_balance() - balansı çap etsin.
    transfer(amount, other_account) - digər hesabın balansına pul köçürsün.
    __str__() - Hesab sahibinin adı və balansı görünsün. Yəni, owner və balance.

"""


class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print('Məbləğ balansda mövcud deyil!')

    def check_balance(self):
        return f"{self.balance} AZN"

    def transfer(self, amount: int, other_account):
        if amount > self.balance:
            print('Daxil edilən məbləğ balansda mövcud deyil!')
        else:
            self.withdraw(amount)
            other_account.deposit(amount)

            print('Transfer əməliyyatı uğurla icra edildi.')

b1 = BankAccount('Adil Yusublu')
b2 = BankAccount('Renad Xasayev')

print(b1.owner)
print(b1.check_balance())

b1.deposit(500)
# b1.withdraw(300)

# print(b1.check_balance())
b1.transfer(200, b2)

print(b1.check_balance())
print(b2.check_balance())
