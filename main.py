# # # funksiyalar usttida mashq qilaman
# #
# # def salom_ber():
# #
# #     """Bu funksiya salom beradiganfunksiya"""
# #     print('Assalomu aleykum')
# # salom_ber()
# #
# # def salom_ber():
# #     """Bu funksiya salom beradigan funksiya"""
# #     print('Assalomu aleykum')
# # salom_ber()
# # salom_ber()
# #
# # def salom_ber(ism):
# #     """Ismni qabul qilib unga salom beruvchi funksiya"""
# #     print(f"Assalomu aleykum, hurmatli {ism.title()}!")
# # salom_ber('Hasan')
# # salom_ber("Charos")
# #
# # def salom_ber(ism, familiya):
# #     """Ism va familiyani qabul qilib, javob qaytaradigan funksiya"""
# #     print(f"Foydalanuvchi ismi: {ism.title()}\n"
# #           f"Foydalanuvchi familiyasi: {familiya.title()}"
# #           )
# # salom_ber('olim', 'hakimov')
# #
# #
# # def toliq_ism(ism, familiya):
# #     """Ism va familiyani qabul qilib javob qaytaradigan funksiya"""
# #     print(f"Foydalanuvchi ismi: {ism.title()}\n"
# #           f"Foydalanuvchi familiyasi: {familiya.title()}")
# # toliq_ism('charos', 'asadova')
#
# def yearsl_old(ism, tugilgan_yil):
#     """Foydalanuvhidan malumotlarni qabul qilib javb qaytaradigan funksiya"""
#     print(f"{ism.title()} yoshingiz {2022-tugilgan_yil}da")
# yearsl_old('Rizamat', 1990)
#
#
# def kvadrat(son):
#     """Sonni kvadrat va kubini hisoblab beradigan funksiya"""
#     print(f"{son} ning kvadrati {son**2}ga teng \n"
#           f"kubi esa {son**3} ga")
# kvadrat(13)
#
# def juft_toq(son):
#     if son%2:
#         print(f"{son} toq")
#     else:
#         print(f"{son} juft")
# juft_toq(10)
# juft_toq(16)
# def juftmi(son):
#     """Kiritilgan son juft yoki toqligini konsolga chiqaruvchi funksiya"""
#     if son%2:
#         print(f"{son} toq son")
#     else:
#         print(f"{son} juft son")
#
#
# juftmi(20)
# juftmi(123)
#

# def katta(a,b):
#     if a>b:
#         print(f"{a} soni {b} dan katta")
#     else:
#         print(f"{a} son {b}dan kichik")
# katta(4,2)
#
# def kvadrat(x,y=2):
#     print(f"{x} ning {y} - darajasi {x**y} ga teng")
# kvadrat(2)


# def bolinish(son):
#     for n in range(2,10):
#         if not son%n:
#             print(f"{son} {n} ga qoldiqsiz bo'linadi")
# bolinish(70)

# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq isma qaytaruvchi funksiya"""
#     if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
# talaba1= toliq_ism_yasa('Abror', 'Olimov')
# talaba2 = toliq_ism_yasa('Nargiza', 'Toxtasinovna', 'Asadova' )
# print(talaba2)
#
# print(f"Bgun darsga kelmagan talaba {talaba1}")
# print(f"Bugun darsda faol qatnashgan talaba {talaba2}dir ")


#Qovushqoqlikni hisoblashda foydalaniladigan interpolyatsiya tenglamasi
#
# X1 = float(input('Birinchi nuqtani kiriting! '))
# X2 = float(input('Ikkinchi nuqtani kiriting! '))
# X = float(input('Oraliq nuqtani kiriting! '))
# Y1 = float(input('Birinchi nuqtaga mos qiymatni kiriting! '))
# Y2 = float(input('Ikkinchi nuqtaga mos qiymatni kiriting! '))
# # Y oraliq nuqtaga mos qiymat ni topish formulasi
#
# Y = Y1 - ((Y1-Y2)*(X-X1)/(X2-X1))
# print(Y)
#
# def salom_ber(ism):
#     print(f"{ism} nega kattalarga sallom bermaysan?!")
# salom_ber('Nargiza')
#
# def kiyim(type, color, size):
#     print(f"mening {type}m rangi {color} o'lchami {size}")
# kiyim('stringi', 'qora', 44)

# def my_function(*kids):
#   print("The youngest child is " + kids[2])
#
# my_function("Emil", "Tobias", "Linus")

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#   print(i, a[i])

# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True

# print('Eng yaqin 5 ta dugonanggiz ismini kiriting!')
# dugonalar = []
# for n in range(5):
#     dugonalar.append(input(f"{n+1} - dugonanggiz ismini kiriting "))
# print(dugonalar)

# print("1 dan 10 gacha bo'lgan sonlar kvadratini hisoblang")
#
# for n in range(10):
#     print(f"{n+1} ning kvadrati  {(n+1)**2}")

# print('dastlabki 5 ta mijozingiz ismini kiriting!')
# mijozlar = []
# for n in range(1, 6):
#     mijozlar.append(input(f"{n} - mijozingizni ismini kiriting "))
# print(mijozlar)
#
# mijozlar.sort()
# print(mijozlar)
# mijozlar2 = tuple(mijozlar)
# print(mijozlar2.)

# country = ['Uzbekistan', 'Russia', 'Litva', 'USA']
# # print(sorted(country, reverse=True))
# print(country)
# country.reverse()
# print(country)
# country.sort()
# print(country)

# numbers = list(range(120, 1200, 2))
# print(numbers)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# print(len(numbers))
# print(f"{max(numbers) - min(numbers)} max va min qiymatlar ayirmasi")
# print(numbers[-20:])

# cars = ['toyota', 'hyundai', 'mazda', 'gm', 'kia']
# for car in cars:
#     if car!='gm':
#
#         print(car.title())
#     else:
#         print(car.upper())

# name = input('Ismingizni kiriting? ')
# ism = name.lower()
# if ism == 'admin':
#     print('Xush kelibsiz' + ' ' + ism.title())
# else:
#     print('Xush kelibsiz' + ' ' + ism.title())
# print('Ikkita son kiriting!')
# a = input('1 - sonni kiriting ')
# b = input('2 - sonni kiritibng ')
# if a == b:
#     print('ikki son teng ekan')
# if a > b:
#     print('1 - son katta')
# if a<b:
#     print('2 - son katta')
# print('istalgan son kiriting ')
# son = int(input('son kiriting '))
# if son >0:
#     print(son**0.5)
# else:
#     print('musbat son kiriting')
#
# print('Hayvonot bogiga kirish chiptalari!')
# yosh = int(input('Yoshingizni kiriting? '))
#
# if yosh <=7 or yosh > 60:
#     print('Siz uchun kirish bepul!')
# elif yosh <18:
#     print('Bilet narxi 6 000 sum!')
# # elif yosh > 60:
# #     print('Siz uchun ham bepul!')
# else:
#     print('Bilet narxi 10 000 sum!')
#
# son = float(input("Juft son kiriting: "))
# if son%2==0:
#     print("Bu son juft.")
# else:
#     print("Bu son juft emas!")

# yosh = int((input("Yoshingiz nechida?")))
#
# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f'{x}<{y}')
# else:
#     print(f"{x}>{y}")

# mahsulotlar = ['un', 'yog', 'sovun', 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#
# savat =[]
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#
# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else:
#     print("Savatingiz bo'sh")

# mahsulotlar = ['un', "yog", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#
# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n + 1}-mahsulotni qo\'shing: '))
#
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
#
#     # if mavjud_emas:
#     #     print("Do'konimizda quyidagi mahsulotlar yo'q:")
#     # for mahsulot in mavjud_emas:
#     #     print(mahsulot)
#     # else:
#     #     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# print(bor_mahsulotlar)
# print(mavjud_emas)
# print(savat)

# users = ['alisher1983','aziza','yasina', 'umar']
#
# login = input("Yangi login tanlang: " )
#
# if login.lower() in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")