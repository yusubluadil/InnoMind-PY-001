# 1. for loop vasitəsi ilə 1-dən 50-yə qədər ədədlərin cəmini tapın.

s = 0
for i in range(1, 51):
    s = s + i

print(s)


# 2. istifadəçinin daxil etdiyi stringin içindəki hərfləri tək-tək çap edin.

user_input = input("Bir string daxil edin: ")

for char in user_input:
    print(char)


# 3. Aşağıdakı kimi üçbucaq çap edin:
#     *
#     **
#     ***
#     ****

for i in range(1, 5):
    print('*' * i)
