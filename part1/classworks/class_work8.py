"""

Morse əlifbası: Tarixi və İstifadə Sahələri

Tarixi:
    Morse əlifbası 1830-cu illərdə amerikalı ixtiraçı Samuel Morse və onun həmkarı Alfred Vail tərəfindən hazırlanmışdır.
    Əsas məqsəd uzaq məsafələrə məlumat ötürmək idi və bu sistem ilk dəfə elektrik telegrafı vasitəsilə tətbiq olunmuşdur.

    Morse əlifbası hər bir hərf, rəqəm və bəzi simvollar üçün nöqtə (·) və tire (–) kombinasyonundan ibarətdir.
    Məsələn, "A" hərfi ·–, "B" isə –··· şəklində kodlanır.

İstifadə Sahələri:
    Morse əlifbası uzun müddət təhlükəsizlik, hərbi və dənizçilik sahələrində istifadə edilmişdir.
    Xüsusilə radio rabitəsi və təcili yardım hallarında ("SOS" siqnalı: ···–––···) önəmli yer tutmuşdur.

Bəzi müasir istifadələr:
    Hava və dəniz nəqliyyatında ehtiyat rabitə vasitəsi kimi;
    Qulaqdan, vizual və ya toxunma əsaslı kommunikasiya metodlarında;
    Radio həvəskarları arasında.

"""

# 1. Latın əlifbası ilə verilmiş mətni Morse əlifbasına çevirən proqram tərtib edin.
# 2. Morse əlifbası ilə verilmiş mətni açan proqram tərtib edin.


# LATIN_TO_MORSE_CODE_DICT = {
#     'A': '.-',     'B': '-...',   'C': '-.-.',
#     'D': '-..',    'E': '.',      'F': '..-.',
#     'G': '--.',    'H': '....',   'I': '..',
#     'J': '.---',   'K': '-.-',    'L': '.-..',
#     'M': '--',     'N': '-.',     'O': '---',
#     'P': '.--.',   'Q': '--.-',   'R': '.-.',
#     'S': '...',    'T': '-',      'U': '..-',
#     'V': '...-',   'W': '.--',    'X': '-..-',
#     'Y': '-.--',   'Z': '--..',
#     '0': '-----',  '1': '.----',  '2': '..---',
#     '3': '...--',  '4': '....-',  '5': '.....',
#     '6': '-....',  '7': '--...',  '8': '---..',
#     '9': '----.',
#     ' ': '/'
# }


# txt = input('Mətni daxil edin: ')

# result = ''
# for i in txt.upper():
#     if i in LATIN_TO_MORSE_CODE_DICT:
#         result += LATIN_TO_MORSE_CODE_DICT[i]
#         result += '/'
#     else:
#         result += '?'

# print(result)


# MORSE_CODE_TO_LATIN_DICT = {v: k for k, v in LATIN_TO_MORSE_CODE_DICT.items()}
# Morse əlifbası ilə yazılan mətn '/' simvolu vasitəsi ilə ayrılır.






"""

Napoleonun Hərbi Məktubları və Gizli Mesajlar

Tarixi Kontekst:
    Napoleon Bonaparte (1769–1821) Fransa imperatoru və dövrünün ən mühüm hərbi liderlərindən biri idi.
    O, Avropada genişmiqyaslı müharibələr apardığı üçün məxfi yazışmalar və gizli rabitə üsulları onun üçün
    həyati əhəmiyyət daşıyırdı.


Gizli mesajlar nəyə görə vacib idi?
    Əmr və göstərişlərin düşmənin əlinə keçməməsi üçün
    Hərbi planların təhlükəsiz ötürülməsi üçün
    Əlaqə qırıldıqda ehtiyat üsul kimi
    Cəsuslara qarşı tədbir kimi

Napoleonun gizli yazışma üsulları:
    Napoleon dövründə məktublar çox vaxt parçalanmış, şifrələnmiş və ya gizli mesajlarla yazılırdı.
    Onun istifadə etdiyi üsullardan bəziləri:
        1. Mətnin içində gizlədilən mesaj
            Məsələn:
            Hər 2-ci və ya 3-cü hərf gizli mesajı təşkil edir
            Hər sətirdəki ilk və ya son hərflər bir mesaj formalaşdırır

        2. Kodlaşdırma sistemləri
            Napoleon və ordusu əlifbanı dəyişdirmə və ya rəqəmlərlə əvəz etmə kimi üsullarla mesajları gizlədirdi.
            Məsələn: "A" = 3, "B" = 7 və s.

        3. Kimyəvi yollarla yazılan görünməz mürəkkəblər
            Bir çox məktubda mesajlar yalnız istiliklə və ya xüsusi maddə ilə görünən mürəkkəblə yazılırdı.

"""


# 1. Napoleonun məktublarını açan proqram tərtib edin.
# SWALKDJKIOPL
# ADIL

txt = 'SWALKDJKIOPL'
result = ''

for i in range(2, len(txt), 3):
    print(i)
    result += txt[i]

print(result)


c = 2
res = ''
while c < len(txt):
    res += txt[c]
    c += 3

print(res)
