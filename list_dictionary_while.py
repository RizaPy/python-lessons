#Lug'at bilan ishlaymiz

# car_0 = {
#     'model':'malibu',
#     'color':'red',
#     'years':'2020',
#     'korobka':'avtomat'
# }
#
# car_1 = {
#     'model':'nexia',
#     'color':'black',
#     'years':'2020',
#     'korobka':'avtomat'
# }
#
# car_2 = {
#     'model':'spark',
#     'color':'white',
#     'years':'2020',
#     'korobka':'mechanik'
# }
# cars = [car_0, car_1, car_2]
# print(cars)


# otam = {
#     'ismi' : 'umar',
#     't_yili' : 1967,
#     'adress' : 'Karakul'
# }
#
# onam = {
#     'ismi' : 'Olmaxon',
#     't_yili' : 1968,
#     'adress' : 'Karakul'
# }
#
# akam = {
#     'ismi' : 'Azamat',
#     't_yili' : 1989,
#     'adress' : 'Karakul'
# }
#
# singlim = {
#     'ismi' : 'Zarina',
#     't_yili' : 1996,
#     'adress' : 'Karakul'
# }
#
# print(f"Dadamning ismi {otam['ismi'].title()},"
#       f"tugilgan yili {otam['t_yili']},"
#       f"tugilgan joyi {otam['adress']} tumani")
#
# print(f"Onamning ismi {onam['ismi'].title()},"
#       f"tugilgan yili {onam['t_yili']},"
#       f"tugilgan joyi {onam['adress']} tumani")
#
# print(f"akamning ismi {akam['ismi'].title()},"
#       f"tugilgan yili {akam['t_yili']},"
#       f"tugilgan joui {akam['adress']} tumani")
#
# print(f"singlimning ismi {singlim['ismi'].title()},"
#       f"tugilgan yili {singlim['t_yili']},"
#       f"tugilgan joui {singlim['adress']} tumani")

#Sevimli taomlar
#
# taomlar = {
#     'dadam' : ['osh', 'manti', 'kabob', 'dimlama', 'shurva'],
#     'onam' :['osh', 'xonim', 'lagman', 'grill', 'shurva'],
#     'akam' : ['somsa', 'kartoshka', 'osh', 'manti', 'baliq']
# }
#
# print(f"dadamning sevmli taomi {taomlar['dadam'][1]}")
# print(f"onamning sevmli taomi {taomlar['onam'][0]}")
# print(f"akamning sevmli taomi {taomlar['akam'][2]}")

#Pythonning izohli lugati
#
# python = {
#     'print' : 'chiqarish funksiyasi',
#     'if' : 'shartni tekshiradigan operator',
#     'and' : 'mantiqiy operator',
#     'for' : 'takrorlanishni taminlovchi operator',
#     'integer' : 'butun sonni ifodolovchi',
#     'floating' : 'o\nli sonni qabul qiluvchu buyruq',
#     'string' : 'satr malumot turini ko\'rsatadi',
#     'while' : 'takrorlanishni taminlovchi operator',
#     'or' : 'mantiqiy operator',
#     'false' : 'yolgon deb tarjima qilinadi'
# }
#
# word = input('Python nomli lugatdagi so\'zni kiriting!')
# for key, volue in python.items():
#     if word == key:
#         print(f"{key}ning tarjimasi {volue}")
# else:
#     print('Bunday soz luhatda yuq')
#     #print(f"{key}ning qiymati {volue}ga  teng")

# capital = {
#     'Uzbekistan' : 'Tashkent',
#     'Russia' : 'Moscow',
#     'France' : 'Parij',
#     'Turkiye' : 'Ankara',
#     'Turkmenistan' : 'Asgabat'
# }

# print('Enter your country?')
# country = input('Enter your country? ')
# for key, volue in capital.items():
#     if country.title() == key:
#         print(f"{key}ning poytaxti {volue} shahri!")
#         break
# else:
#     print('Bunday davlat haqida bizda ma\'lumot yuq!')
#
#
# for k, q in sorted(capital.items()):
#     print(capital)
# print(capital)
#

# davlatlar = {
#     "o'zbekiston": "toshkent",
#     "aqsh": "washington d.c.",
#     "rossiya": "moskva",
#     "tojikiston": "dushanbe",
#     "qirg'iziston": "bishkek",
#     "qozog'iston": "nursulton",
#     "malayziya": "kuala-lumpur",
#     "singapur": "sungapur",
#     "italiya": "rim",
# }
#
# print("Dunyo davlatlari:")
# for davlat in sorted(davlatlar):
#     print(davlat.upper())
#
# print("\nDavlatlarning poytaxtlari")
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())
#
# country = input("Qaysi davlatning poytaxtini bilishni istaysiz?:").lower()
# capital = davlatlar.get(country)
# if capital == None:
#     print("Kechirasiz, bizda bu haqida ma'lumot yo'q")
# else:
#     print(f"{country.upper()}ning poytaxti {capital.title()} shahri")

# print('10 gacha bulgan sonlar yogisdisini aniqlang!')
# s = 0
# i = 0
# while i<=10:
#     s = s+i
#     i+=1
# print(s)
#
#
# s = 1
# i = 1
#
# while i<=10:
#     s = s*i
#     i = i+1
# print(s)



