# 3.​ [3, 7, 12, 25, 8, 14, 19, 33, 6, 21, 27, 10] kimi bir list var. Bu listdə
# olan ədədlərin ədədi ortasını tapın.

numbers = [3, 7, 12, 25, 8, 14, 19, 33, 6, 21, 27, 10]

average = sum(numbers) / len(numbers)
rounded_avarage = round(average, 2) # Daxil edilmiş ədədi nöqtədən sonra 2 ədəd saxlayaraq yuvarlaqlaşdırır.

print(average)
print(rounded_avarage)


# 1.​ fruits = ['apple', 'banana', 'cherry', 'orange'] kimi bir list var.
# İstifadəçinin daxil edəcəyi məlumatı listdən silin.
# (Qeyd: İstifadəçi yalnız listdə olan məlumatlardan birini daxil edəcək.)


fruits = ['apple', 'banana', 'cherry', 'orange']

fruit_name = input("Silinməsini istədiyiniz meyvəni daxil edin: ")

if fruit_name in fruits:
    fruits.remove(fruit_name)
else:
    print("Bu meyvə listdə yoxdur.")

print(fruits)
