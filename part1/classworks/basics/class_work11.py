# 1. Sözlərin sayını qaytaran funksiya.

# 2. Ən çox təkrarlanan hərfin sayını qaytaran funksiya.

def get_letter_count(*, txt):
    words_count = {}

    for letter in txt.lower():
        words_count[letter] = words_count.get(letter, 0) + 1

    max_count_letter = None
    max_count = 0

    for letter, count in words_count.items():
        if count > max_count:
            max_count = count
            max_count_letter = letter

    return max_count_letter

string = input('Mətni daxil edin: ')
print(get_letter_count(txt=string))



def get_letter_count(*, txt):
    words_count = {}

    for letter in txt.lower():
        words_count[letter] = words_count.get(letter, 0) + 1

    sorted_counts = sorted(words_count.items(), key=lambda items: items[1], reverse=True)
    return sorted_counts[0][0]


string = input('Mətni daxil edin: ')
print(get_letter_count(txt=string))
