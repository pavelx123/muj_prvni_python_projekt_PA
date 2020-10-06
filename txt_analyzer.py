'''
author = Pavel Šumichrast 5.10.2020
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]


print('Vítej uživateli,')
print('=' * 20)
jmeno = input('Zadej svoje jméno: ')
heslo = input('Zadej svoje heslo: ')

registrovani_uzivatele = {'bob' : '123', 'ann' : 'pass123', 'mike' : 'password123', 'liz' : 'pass123'}
if jmeno in registrovani_uzivatele.keys():
    if heslo in registrovani_uzivatele.values():
        print('Vítej Bobe jsi uvnitř!')
    else:
        print('Bobe nemáš správné heslo!')
else:
    print('Tvoje jméno nebo heslo je nesprávné.')

oddelovac = "=" * 1
print(oddelovac*76)
vyber = int(input('Máme 3 texty k analyzování, zadej číslo od 1 do 3, který z textů si vybereš: '))
print(oddelovac*76)

if vyber == 1:
    #print(TEXTS[0])
    vyber_1 = TEXTS[0]
    print(vyber_1)
elif vyber == 2:
    #print(TEXTS[1])
    vyber_2 = TEXTS[1]
    print(vyber_2)
elif vyber == 3:
    #print(TEXTS[2])
    vyber_3 = TEXTS[2]
    print(vyber_3)
else:
    print('Zadal jsi špatné číslo, zadej znovu (rozmezí 1 - 3)!')

# Spočtení slov ve vybraném textu:
print(oddelovac*40)
if vyber == 1:
#if vyber_1:
    rozdelena_slova = TEXTS[0].split()
    print('Přehled jednotlivých neočištěných slov: ', rozdelena_slova)
elif vyber == 2:
#elif vyber_2:
    rozdelena_slova = TEXTS[1].split()
    print('Přehled jednotlivých neočištěných slov: ', rozdelena_slova)
else:
    rozdelena_slova = TEXTS[2].split()
    print('Přehled jednotlivých neočištěných slov: ', rozdelena_slova)



ocistena_slova = []

'''
while rozdelena_slova:
    nactena_slova = rozdelena_slova.pop()
    ocistena_slova.append(nactena_slova.strip(",."))

print(ocistena_slova)
'''
print(oddelovac*40)
ocistena_slova = [nactena_slova.strip(",.") for nactena_slova in rozdelena_slova]
print('Přehled očištěných slov: ', ocistena_slova)

# Zobrazení počtu slov v proměnné:
print(oddelovac*24)
print('Počet slov ve vybraném textu je:', len(ocistena_slova))

# Zobrazení počtu jednotlivých slov:
print(oddelovac*43)
vyskyt_slov = {}

for slovo in ocistena_slova:
    vyskyt_slov[slovo] = vyskyt_slov.get(slovo, 0) +1

print('Přehled četnosti výskytu jednotlivých slov: ', vyskyt_slov)
print('\n')

# Zobrazení výskytu jednotlivých slov :
print(oddelovac*53)
print('PŘEHLEDNÁ TABULKA ČETNOSTI VÝSKYTU JEDNOTLIVÝCH SLOV:')
print(oddelovac*53)
for x in ocistena_slova:
  print(f"SLOVO: *{x}*, VYSKYT: {vyskyt_slov[x]}x")

'''
# Pomocí comprehension:
pocet_vyskytu = [(f"SLOVO: *{x}*, VYSKYT: {vyskyt_slov[x]}x") for x in ocistena_slova]
pocet_vyskytu
'''


print(type(ocistena_slova))

# Počet slov ve vybraném článku:
print(len(ocistena_slova))

print(oddelovac*50)
if vyber == 1:
    vyber = TEXTS[0]
    def pocet_velkych_pismen(vyber):
        rozdelena_slova = TEXTS[0].split()
        total_count = 0
        for letter in vyber[1:]:
            if letter.isupper():
                total_count += 1
        return total_count

    print('Počet velkých písmen vybraného odstavce: ',  pocet_velkych_pismen)
elif vyber == 2:
    vyber = TEXTS[1]
    def pocet_velkych_pismen(vyber):
        rozdelena_slova = TEXTS[1].split()
        total_count = 0
        for letter in vyber[1:]:
            if letter.isupper():
                total_count += 1
        return total_count
    print('Počet velkých písmen vybraného odstavce: ', pocet_velkych_pismen)
elif vyber == 3:
    vyber = TEXTS[2]
    def pocet_velkych_pismen(vyber):
        rozdelena_slova = TEXTS[1].split()
        total_count = 0
        for letter in vyber[1:]:
            if letter.isupper():
                total_count += 1
        return total_count
    print('Počet velkých písmen vybraného odstavce: ', pocet_velkych_pismen)

print(oddelovac*50)

# Počet slov psaných velkými písmeny:
for x in vyber:
    print('Počet slov která jsou celá velká', x.isupper())

# Počet slov psaných malými písmeny:
for x in vyber:
    print('Počet slov která jsou celá velká', x.islower())

# Zatím víc nedokážu, ale postupně !!!
