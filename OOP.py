# class Phone:

#     def __init__(self, name:str, colour:str, price:int):
#         self.name = name
#         self.colour = colour
#         self.price = price

#     def getName(self):
#         return self.name
    
#     def getPrice(self):
#         return self.price
    
#     def getColour(self):
#         return self.colour

#     def __str__(self):
#         return f"Nomi: {self.name}\nRangi: {self.colour}\nNarxi: {self.price}"
    
# ph = Phone('Samsung', 'Qora', 1500)
# print(ph)

""" Home Work"""
# 1 = car haqida
# 2 = programmer haqida
# 3 = file haqida  


""" HOMEWORK """
# class Car:

#     def __init__(self, model:str, yil:str, narx:str):
#         self.model = model
#         self.yil = yil 
#         self.narx = narx

#     def getModel(self):
#         return self.model
#     def getYil(self):
#         return self.yil
#     def getNarx(self):
#         return self.narx
        
#     def __str__(self):
#         return f"Nomi: {self.model}\nNarxi: {self.narx}\nYili: {self.yil}"
    
# cr = Car('Mers', 2022, 120000)
# cr1 = Car('Malibu', 2020, 20000)
# cr2 = Car('Spark', 2018, 10000)
# cr3 = Car('Porsh', 2022, 120000)
# cr4 = Car('G Class', 2023, 200000)
# cr5 = Car('Zaparosh', 1980, 5000)
# cr6 = Car('Jiguli', 2002, 7000)
# cr7 = Car('Malibu 2', 2022, 15000)
# cr8 = Car('Tesla', 2022, 200000)
# cr9 = Car('Amg', 2023, 300000)
# print(cr)


""" Programmer """
# class Programmer:

#     def __init__(self, tarjima:str, kasb:str, soha:str,):
#         self.tarjima = tarjima
#         self.kasb = kasb
#         self.soha = soha

#     def getTarjima(self):
#         return self.tarjima
    
#     def getKasb(self):
#         return self.soha
    
    # def getSoha2(self):
    #     return self.soha2

    # def fullInfo(self):
    #     return f"Programmer: {self.tarjima}\nKasbi: {self.kasb}\nSohasi: {self.soha}"
    
    # def __str__(self):
        # return self.name
    
# pr = Programmer('Dasturchi', 'Dasturchi', 'Web Dasturlash')
# pr1 = Programmer('Programist', 'Dastur Yaratish', 'Web Dizayner')
# pr2 = Programmer('Dasturchi', 'Sayt yaratish', 'Backend')
# pr3 = Programmer('Bot Yaratuvchi', 'Bot Yaratish', 'Frontend')
# pr4 = Programmer('Sayt Yaratuvchi', 'Sayt yaratish', '1C')
# pr5 = Programmer('Model', 'Model Yaratish', 'Model')
# pr6 = Programmer('Dizayner', 'Dizayn Tuzuvchi', 'Dizayner')
# pr7 = Programmer('Mobilogrof', 'Mobile Dasturlar', 'Mobile Dasturchi')
# pr8 = Programmer('Oyin Yaratuvchi', 'Oyin Yaratuvchi', 'Oyin Yaratish')
# pr9 = Programmer('Maket Tuzuvchi', 'Arhitektor', 'Maket Chizish')
# print(pr, pr6)


""" File """
# class File:

#     def __init__(self, nomi:str, yili:int, nout:str):
#         self.nomi = nomi
#         self.yili = yili
#         self.nout = nout

#     def getNomi(self):
#         return self.nomi
    
#     def getYili(self):
#         return self.yili
    
#     def getNout(self):
#         return self.nout
    
#     def __str__(self):
#         return f"File Nomi: {self.nomi}\nChiqqan Yili: {self.yili}\nNoutbuk Nomi: {self.nout}"
    
# fl = File('Windows', 2022, 'Acer')
# fl1 = File('Windows 10', 2021, 'Hp')
# fl2 = File('Windows 7', 2016, 'Victus')
# fl3 = File('Mac', 2022, 'Macbook')
# fl4 = File('Linux', 2022, 'Lenovo')
# fl5 = File('Ubuntu', 2023, 'Sync')
# fl6 = File('Pustoy File', 2023, 'Acer')
# fl7 = File('Azim Qurbonov', 2023, 'Acer')
# fl8 = File('OOP', 2023, 'Acer')
# fl9 = File('English', 2023, 'Hp')
# print(fl7)


""" Rim Raqamlari """
# n = (input('Rim raqamlari kiriting: ')).upper()
# s = 0
# d = {
#     'I' : 1,
#     'V' : 5,
#     'X' : 10,
#     'L' : 50,
#     'C' : 100,
#     'D' : 500,
#     'M' : 1000
# }
# for i in range(len(n) - 1):
#     if d[n[i]] < d[n[i + 1]]:
#         s -= d[n[i]]
#     else:
#         s += d[n[i]]
# s += d[n[-1]]
# print(s)


# class Transport:

#     def __init__(self, model:str, max_speed, created:str):
#         self.model = model
#         self.max_speed = max_speed
#         self.created = created

#     def getModel(self):
#         return self.model
    
#     def getMax_speed(self):
#         return self.max_speed
    
#     def getCreated(self):
#         return self.created
    
#     def getFullinfo(self):
#         return f"Model: {self.model}\nYuqori Tezlig: {self.max_speed}\nIshlab Chiqarilgan Yil: {self.created}"
    
#     def __str__(self):
#         return self.model
    
# class Motorbyke(Transport):

#     def __init__(self, model: str, max_speed, created: str, colour:str, price:int):
#         super().__init__(model, max_speed, created)
#         self.colour = colour
#         self.price = price

#     def getColour(self):
#         return self.colour
    
#     def getPrice(self):
#         return self.price
    
#     def getFullinfo(self):
#         return super().getFullinfo()
    
#     def __str__(self):
#         return super().__str__()
    
# class Car(Transport):

#     def __init__(self, model: str, max_speed, created: str, price:int, type:str):
#         super().__init__(model, max_speed, created)
#         self.price = price
#         self.type = type

#     def getPrice(self):
#         return self.price
    
#     def getType(self):
#         return self.type

#     def getFullinfo(self):
#         return super().getFullinfo()
    
#     def __str__(self):
#         return super().__str__()

# zapcast = Car('G Class', 20000, '12:16:2023', 250000, 'Avtomat')
# print(zapcast.getFullinfo())


""" Homework """
# import math

# class Shape:

#     def __init__(self, colour:str):
#         self.colour = colour
    
#     def getColour(self):
#         return self.colour
    
#     def __str__(self):
#         return self.colour
    
# class Circle(Shape):

#     def __init__(self, colour: str, a:float, area:float):
#         super().__init__(colour)
#         self.a = a
#         self.area = area

#     def getA(self):
#         return self.a
    
#     def getArea(self):
#         return self.area
    
#     def getInfo(self):
#         return math.pi * pow(self.area, 2)
    
#     def __str__(self):
#         return super().__str__()
    
# class Rectangle(Shape):

#     def __init__(self, colour: str, length:float, width:float):
#         super().__init__(colour)
#         self.length = length
#         self.width = width

#     def getLength(self):
#         return self.length
    
#     def getWidth(self):
#         return self.width
    
#     def getFullinfo(self):
#         return self.length * self.width
    
#     def __str__(self):
#         return super().__str__()
    
# ph = Circle('Green', 12.45, 7.0)
# print(ph.getInfo())


"""  1chi exercise """
# class Car:

#     def __init__(self, name:str, colour:str, speed:int):
#         self.name = name
#         self.colour = colour
#         self.speed = speed
    
#     def getFullInfo(self):
#         return f"{self.colour} rangli {self.name} tezligi {self.speed}ga teng"
    
#     def __str__(self):
#         return self.getFullInfo()

# l = Car('Lacetti', 'Oq', 220)
# m = Car('Malibu', 'Qora', 260)
# k = Car('Matiz', 'Kulrang', 180)
# print(l.getFullInfo())
# print(m.getFullInfo())
# print(k.getFullInfo())


""" 2chi exercise """
# class Phone:

#     def __init__(self, name:str, colour:str, price:float):
#         self.name = name
#         self.colour = colour
#         self.price = price 
    
#     def getName(self):
#         return self.name
    
#     def getColour(self):
#         return self.colour
    
#     def getPrice(self):
#         return self.price
    
#     def setName(self, name):
#         self.name = name
    
#     def setColour(self, colour):
#         self.colour = colour

#     def setPrice(self, price):
#         self.price = price

#     def getInfo(self):
#         return f"Nomi: {self.name}\nRangi: {self.colour}\nNarxi: {self.price}"
    
#     def __str__(self):
#         return self.getInfo()
    
# ph = Phone('Redmi Note4X', 'Qora', 150)
# ph1 = Phone('iPhoneX', 'Oq', 700)
# print(ph.getInfo())
# print(ph1.getInfo())

# class A:

#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh
#     @property
#     def getFullInfo(self):
#         return f"Ismi: {self.ism}\nYoshi: {self.yosh}"
    
#     def __str__(self):
#         return self.ism
    
# obj = A('Billie', 22)
       


# class Father:

#     def __init__(self, ism, familiya, ocestva, yosh):
#         self.ism = ism
#         self.familiya = familiya
#         self.ocestva = ocestva
#         self.yosh = yosh

#     def getFullInfo(self):
#         return f"Ismi: {self.ism}\nFamiliyasi: {self.familiya}\nOcestvasi: {self.ocestva}\nYoshi: {self.yosh}"
    
#     def __str__(self):
#         return self.getFullInfo()
    
# class BigChild(Father):

#     def __init__(self, ism, familiya, ocestva, yosh, gender):
#         super().__init__(ism, familiya, ocestva, yosh)
#         self.__gender = gender

#     def getGender(self):
#         return self.__gender
    
#     def getFull(self):
#         return f"Ismi: {self.ism}\nFamiliyasi: {self.familiya}\nOcestvasi: {self.ocestva}\nYoshi: {self.yosh}\nPol: {self.__gender}"
    
#     def __str__(self):
#         return super().__str__()
    
# obj = BigChild('Ali', 'Valiev', 'Ganievich', 16, 'Erkak')
# print(obj.getFull())
    


""" Homework """

# class Passenger:

#     def __init__(self, passportID, fullName, gender):
#         self.passportID = passportID
#         self.fullName = fullName
#         self.gender = gender
    
#     def getFullName(self):
#         return self.fullName
    
#     def getGender(self):
#         return self.gender
    
#     def setFullName(self, full):
#         self.fullName = full
    
#     def getFullInfo(self):
#         return f"Passport ID: {self.passportID}\n\tFull Name: {self.fullName}\n\tGender: {self.gender}"
    
#     def __str__(self):
#         return self.getFullInfo()
    
# ps1 = Passenger('AB123405', 'Nodir Botirov Qodirovich', 'Erkak')
# ps2 = Passenger('AB236506', 'Botir Nodirov Qodirovich', 'Erkak')

# class Driver:

#     def __init__(self, passportID, fullname, age):
#         self.passportID = passportID
#         self.fullname = fullname
#         self.age = age

#     def getFullName(self):
#         return self.fullname

#     def getAge(self):
#         return self.age

#     def setFullName(self, full):
#         self.fullname = full

#     def setAge(self, yosh):
#         self.age = yosh

#     def getFullInfo(self):
#         return f"Passport ID: {self.passportID} Full Name: {self.fullname} Yoshi: {self.age}"

#     def __str__(self):
#         return self.fullname

# dr = Driver('BA123409', 'Ali Valiyev Sobirovich', 29)

# class Train:

#     def __init__(self, trainID, name, speed, dr):
#         self.trainID = trainID
#         self.name = name
#         self.speed = speed
#         self.dr = dr
    
#     def getName(self):
#         return self.name
    
#     def getSpeed(self):
#         return self.speed
    
#     def setName(self, ism):
#         self.name = ism
    
#     def setSpeed(self, tezlik):
#         self.speed = tezlik

#     def getFullInfo(self):
#         return f"Poezd ID: {self.trainID}\n\tPoezd Nomi: {self.name}\n\tPoezd Tezligi: {self.speed}\n\tHaydovchi: {self.dr}"
    
#     def __str__(self):
#         return self.getFullInfo()
    
# poezd = Train('ABC123456', 'UZB TRAIN', 200, dr)

# class Platform:

#     def __init__(self, platformID, status):
#         self.platformID = platformID
#         self.status = status

#     def getPlatformID(self):
#         return self.platformID
    
#     def setPlatformID(self, platfrom):
#         self.platformID = platfrom

#     def getFullInfo(self):
#         return f"Platfroma ID: {self.platformID}\n\tStatus: {self.status}"
    
#     def __str__(self):
#         return self.getFullInfo()
    
# platforma = Platform('ABC120905', True)

# class Trip:

#     def __init__(self, from1, to, poezd, platforma, passeger, priceTrip, dataTrip):
#         self.from1 = from1
#         self.to = to
#         self.poezd = poezd
#         self.platforma = platforma
#         self.passenger: list = passeger
#         self.priceTrip = priceTrip
#         self.dataTrip = dataTrip

    
#     def addPassenger(self, passenger_obj:Passenger):
#         self.passenger.append(passenger_obj)

#     def getFrom1(self):
#         return self.from1
    
#     def setFrom1(self, frm):
#         self.from1 = frm

#     def getPoezd(self):
#         return self.poezd
    
#     def setPoezd(self, pzd):
#         self.poezd = pzd
    
#     def getFullInfo(self):
#         step = 'Passengers:\n\t'
#         for i, value in enumerate(self.passenger, 1):
#             step += f"{i}- passenger:\n\t {value}\n\t"        
#         return f"From: {self.from1}\nTo: {self.to}\nPoezd: {self.poezd}\nPlatform: {self.platforma}\n{step}\nTrip Narxi: {self.priceTrip}\nTrip Sanasi: {self.dataTrip}"
    
#     def __str__(self):
#         return self.getFullInfo()
    
# pslst = [ps1, ps2]
# trip1 = Trip('Toshkent', 'Andijon', 'Afrosiob', platforma, pslst, 200, '17.06.2023')
# trip2 = Trip('Paris', 'Moscow', 'Afrosiob', platforma, pslst, 300, '17.06.2023')
# lst = [trip1, trip2]
# print(trip1)

# class RailwayStation:

#     def __init__(self, name, adress, lst):
#         self.name = name
#         self.adress = adress
#         self.lst: list = lst
    
#     def addTrips(self, trips_obj: Trip):
#         self.lst.append(trips_obj)

#     def getName(self):
#         return self.name
    
#     def setName(self, ism):
#         self.name = ism

#     def getFullInfo(self):
#         step = 'Sayohatlar:\n\t'
#         for i, value in enumerate(self.lst, 1):
#             step += f"{i}- sayohat:\n\t {value}\n\t"
#         return f"Nomi: {self.name}\n\tManzil: {self.adress}\n\tSayohat: {step}"
    
#     def __str__(self):
#         return self.getFullInfo()
    
# station = RailwayStation('Shimoliy Stansiya', 'Qoraqamish', lst)
# print(station)





# class Coin:

#     def __init__(self, value:int):
#         self.value = value
    
#     def getValue(self):
#         return self.value
# coin1 = 15
# coin2 = 20
# coin3 = 30
# coins = [coin1, coin2, coin3]

# class PaperMoney:

#     def __init__(self, value:int):
#         self.value = value
    
#     def getValue(self):
#         return self.value

# money = 15000
# money1 = 20000
# money3 = 30000
# allmoney = [money1, money1, money3]


# class Wallet:

#     def __init__(self):
#         self.all_money = []

#     def addAllMoney(self, money:PaperMoney|Coin):
#         self.all_money.append(money)
    
#     def getAllPaperMoney(self):
#         s = 0
#         t = 0
#         for i in self.all_money:
#             if isinstance(i, PaperMoney):
#                 t += int(i.value)
#                 s += 1
#         return f"{s} : {t}"
    
#     def getAllCoin(self):
#         s = 0
#         t = 0
#         for i in self.all_money:
#             if isinstance(i, Coin):
#                 t += int(i.value)
#                 s += 1
#         return f"{s} {t}"

#     def getSumMoney(self):
#         r = 0
#         for i in self.all_money:
#             r += i
#         return r

# a = Wallet()
# a.addAllMoney(coins)
# a.addAllMoney(allmoney)
# print(a.getSumMoney())    
# print(a.getAllCoin())
# print(a.getAllPaperMoney())


""" Homewrok """

# class Author:

#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     def getFullName(self):
#         return f"{self.first_name} {self.last_name}"
    
#     def __str__(self):
#         return self.getFullName()
    
# auth = Author('Said', 'Athamov')
# auth1 = Author('Xudoyberdi', 'To\'xtaboev')
# auth2 = Author('Haruki', 'Murakami')
# auth3 = Author('Gabriel', 'Adres')
# auth4 = Author('Joanna', 'Rouling')
# auth5 = Author('Uilyam', 'Shakespeare')

# class Book:

#     def __init__(self, name:str, page_size:int, authors:list):
#         self.name = name
#         self.page_size = page_size
#         self.authors = authors

#     def getAuthors(self, yolovchi:Author):
#         self.authors.append(yolovchi)

#     def getAuthors1(self):
#         f = 'Aftorlar:\n\t'
#         for i, aut in enumerate(self.authors, 1):
#             f += f"{i}- aftor {aut}\n\t"
#         return f
    
#     def getName(self):
#         return self.name
    
#     def __str__(self):
#         f = '\n\tYozuvchilar:\n\t'
#         for i, yol in enumerate(self.authors, 1):
#             f += f"{i}-yozuvchi {yol}\n\t"
#         return f 

# authlist = [auth, auth1, auth2, auth3, auth4, auth5]
# book1 = Book('Harry Potter', 360, [auth, auth1])
# book2 = Book('Malinovaya Lada', 120, authlist)
# book3 = Book('Bussines', 100, authlist)
# book4 = Book('Rich Father and Poor Father', 150, authlist)

# class Library:

#     def __init__(self, name:str, adress:str, books):
#         self.name = name
#         self.adress = adress
#         self.books:list = books

#     def getName(self):
#         return f"Kutubxona Nomi: {self.name}"
    
#     def getAdress(self):
#         return f"Kutubxona Manzili: {self.adress}"
    
#     def getAllBooks(self, kitob_obj:Book):
#         self.books.append(kitob_obj)
    
#     def addBooks(self, *args:Book):
#         for i in args:
#             self.books.append(i)
    
#     def __str__(self):
#         f = 'Kitoblar:\n\t'
#         for i, ktb in enumerate( self.books, 1):
#             f += f"\n{i}-kitob nomi: {ktb.getName()}\n\t{ktb.getAuthors1()}\n-----------------------------"
#         return f

# kitoblar = [book1, book2, book3, book4]
# ktxona = Library('Alisher Navoiy', 'Chorsu', kitoblar)
# ktxona2 = Library('Beruniy', 'Milliy Universitet', kitoblar)
# print(ktxona)



# from pathlib import Path

# p = Path()
# print(p.cwd())


# p = Path('exaam')
# p.mkdir()

# p = Path('giga.py')
# p.touch(exist_ok=False)

# import os 

# while True:
#     if os.system(input(">> ")) != 0:
#         break

# exec('a = 2; b = 3; print(eval(\'a + b\'))')
# print(type(eval('2 + 4 * 5')))



import os
# os.abort()
# os.access('ecam.txt', 0)
# a = os.add_dll_directory('papka')
# os.chdir()
# print(os.environ)
# os.rmdir('papa.txt')

# print(os.path.abspath('keks.txt'))
# os.rename('keks.txt', 'test.txt')



""" Homework """
# import random
# import os
# from time import sleep
# c = '\U0001F695'
# r = '\U0001F697'
# q = '\U0001F699'
# s = ' '
# d = ' '
# e = ' '
# uzunlik = os.get_terminal_size().columns - 3
# while True:
#     os.system('cls')
#     a = s + c
#     if len(a) < uzunlik:
#         s += ' ' * random.randint(1, 3)
#     b = d + r
#     if len(b) < uzunlik:
#         d += ' ' * random.randint(1, 3)
#     m = e + q
#     if len(m) < uzunlik:
#         e += ' ' * random.randint(1, 3)  
#     print(a)
#     print(b)
#     print(m)
#     sleep(0.2)
#     if len(a) >= uzunlik and len(b) >= uzunlik and len(m) >= uzunlik:
#         break
    


from time import sleep
from itertools import groupby, chain, count, cycle, dropwhile, takewhile

# m = [i for i in range(1, 11)]
# x = groupby(m, key=lambda x: x > 5)
# for i, k in x:
#     print(i, list(k))


# x = [12, 23, 45]
# s = {'s', 'a', 'l'}
# t = (12, 34, 9)
# print(list(chain(x, s, t)))


# c = count(10, 10)
# for i in range(20):
#     print(next(c))
    

# def myf():
#     n = 1
#     while True:
#         yield n
#         n += 1
# x = myf()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# s = ["ali", "vali", "bobur"]
# x = cycle(s)
# for i in range(10):
#     print(f"{i + 1}: {next(x)}")


"""dropwhile"""

# x = [12, 23, 45, 67]
# s = dropwhile(lambda x: x > 5, x)
# print(list(s))

"""takewhile"""

# d = [1, 2, 3, 4, 5, 6, 10]
# f = list(takewhile(lambda x: x > 5, d))
# print(f)






""" COLLECTIONS """


# def adjacentElementsProduct(inputArray):
#     for i in range(0, len(inputArray)-1):
#         lis=(inputArray[i]*inputArray[i+1])
#     return lis
# lst = [5, 1, 2, 3, 1, 4]
# print(adjacentElementsProduct(lst))
    
# def adjacent_elements_product(array):
#     max_product = float('-inf')
    
#     for i in range(len(array)-1):
#         product = array[i] * array[i+1]
#         if product > max_product:
#             max_product = product
    
#     return max_product
# ls = [5, 1, 2, 3, 1, 4]
# print(adjacent_elements_product(ls))

# def son_top(n):
#     return n ** 2 + (n - 1) ** 2

# print(son_top(3))

# ls = [12, 34, 45]
# print(ls.index(34))

# print('ComputerScience'.removesuffix('Science'))
# print('SalomPython'.removesuffix('Python'))
# print('Salompython'.removeprefix('Salom'))


# tr = 'salom'
# print(tr.endswith('m'))
# print(tr.startswith('sa'))


    