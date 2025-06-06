# Dictionary (Dict) - Açar və dəyər (key, value) cütlərindən ibarət məlumatları saxlayır
# {'key1': 'value1', 'key2': 'value2', ...}
# Dict - Sıralıdır.
# Dict - Dəyişiləndir.
# Dict - Index yerinə key-lərdən istifadə olunur.
# Dict - Keylər unikal(təkrarlanmaz) olur.


# dt1 = {}
# dt2 = dict()

# print(type(dt1))  # <class 'dict'>
# print(type(dt2))  # <class 'dict'>


# bio = {'name': 'Renad', 'surname': 'Xasayev'}

# print(bio['name'])
# print(type(bio['name']))

# print(bio['surname'])

# bio['name'] = 'Adil'
# bio['surname'] = 'Yusubov'
# print(bio)
# # print(bio['age']) # age key-i olmadığı üçün error verəcək

# bio['age'] = 22
# print(bio)


# user_cards = {
#     "name": "Ədil",
#     "surname": "Həsənquliyev",
#     "age": 19,
#     "is_student": True,
#     "courses": ["Python", "JavaScript", "C++"],
#     "address": {
#         "city": "Bakı",
#         "country": "Azərbaycan"
#     },
# }

# print(user_cards)
# print(user_cards['address']['city'])  # Bakı

# print(user_cards['courses'][-1])

# user_cards['is_student'] = False
# print(user_cards['is_student']) # False




# Dict methods

currencies = {
    "USD": {
        "name": "Amerika Birləşmiş Ştatları Dolları",
        "symbol": "$",
        "rate": 1.0
    },
    "EUR": {
        "name": "Avro",
        "symbol": "€",
        "rate": 0.85
    },
    "GBP": {
        "name": "Britaniya Funtu",
        "symbol": "£",
        "rate": 0.75
    }
}


# 1. clear() - Dict-i təmizləyir

# print(currencies)

# currencies.clear()
# print(currencies)  # {}


# 2. copy() - Dict-in surətini çıxarır

copied_currencies = currencies.copy()
# print(currencies)  # {'USD': {'name': 'Amerika Birləşmiş Ştatları Dolları', 'symbol': '$', 'rate': 1.0}, ...}
# print(copied_currencies)  # {'USD': {'name': 'Amerika Birləşmiş Ştatları Dolları', 'symbol': '$', 'rate': 1.0}, ...}


currencies['USD'] = None
print(currencies)  # {'USD': {'name': 'Amerika Birləşmiş Ştatları Dolları', 'symbol': '$', 'rate': 1.1}, ...}
print(copied_currencies)  # {'USD': {'name': 'Amerika Birləşmiş Ştatları Dolları', 'symbol': '$', 'rate': 1.1}, ...}
