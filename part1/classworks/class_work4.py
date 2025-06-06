# Istifadəçinin daxil etdiyi məlumatın DB adlı dictdə açar olub-olmamasını yoxlayın.
# Əgər varsa, dəyərini ekrana çap edin. Əks halda, "Açar tapılmadı" mesajını verin.

DB = {
    "name": "Ədil",
    "surname": "Həsənquliyev",
    "age": 19,
    "is_student": True,
    "courses": ["Python", "JavaScript", "C++"],
    "address": {
        "city": "Bakı",
        "country": "Azərbaycan"
    },
}


key = input("Açarı daxil edin: ")

if key in DB:
    print(f"{key} açarının dəyəri: {DB[key]}")
else:
    print("Açar tapılmadı")
