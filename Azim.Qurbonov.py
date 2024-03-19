"""
date: 22.05.2023
student: Azim Qurbonov
direction: PYTHON
theme: Rewiev  
"""

import random
from typing import Any
# print('Nima eksang shuni o\'rasan !, \nAlbatta ha !')
# print('''Nima eksang shuni orasan !
# Ha albatta''')

# print('Hello my name is Azim. \nI\' m 15 years old. \nI\' student')

# print(pow(2, 3) / 4)
# print( 2 + 3 - 5)
# print(10 // 2)
# print(10 % 2)
# print(15 / 3)


# i = 1
# while i <= 10:
#     print(f"{i} * {i} == {i ** 2}")
#     i += 1

# for i in range(1, 11):
#     print(f"{i} * {i} = {i ** 2}")


# def myf(*args):
#     for i in range(1, n + 1):
#         print(f"{i} * {i} = {pow(i, 2)}")
#     return 'Hello World'
# n = int(input('Son kiriting: '))
# print(myf(n))
        

# num = lambda num: (num + 10) / 2
# print(num(10))

# m = [1, 2, 3, 4, 5, 6, 7, 8, 10]
# x = list(filter(lambda x: x % 2 == 0, m))
# print(x)


# m = [1, 2, 3, 4, 5, 6, 7, 8, 10]
# x = list(map(lambda x: x % 2, m))
# print(x)


# a = int(input('Son kiriting: '))
# b = int(input('Son kiriting: '))
# for i in range(a, b + 1):
#     print(i, end=' ')

# a = int(input('Son kiriting: '))
# b = int(input('Son kiriting: '))
# for i in range(a, b + 1):
#     print(i, end=' ')


# lst = [random.randint(1, 10) for i in range(5)]
# print(lst)
# lst = [1, 2, 3, 4, 5]
# x = list(map(lambda x: x % 2 == 0 and x ** 2, lst))
# print(x) 

# def func(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return func(n - 1) + func(n - 2)
# print(func(9))

# d = [1, 33, 4, 5, 6, 34, 8, 10, 11]
# m = [1, 3, 4, 5, 6, 7, 89, 98, 23]
# x = list(zip(d, m))
# print(x)


# a = int(input('Son kiriting: '))
# b = int(input('Son kiriting: '))
# for i in range(a, b + 1):
#     print(i, end=' ')

"""
List Tuple (list) va (o'zgarmas listlar(tuple))
"""

# davlatlar = ['Usa', 'Uk', 'uzbek']
# cars = ['bmw', 'mers', 'audi']
# print(davlatlar.count(davlatlar[1]))  # (count) listdagi element sonini qaytaradi
# print(davlatlar.index(3))
# print(davlatlar.clear())
# davlatlar.insert(1, 'uzbekistan')
# print(davlatlar)
# davlatlar.extend(cars)
# print(davlatlar)
# davlatlar.sort()
# print(davlatlar)
# x = davlatlar.pop(1)    
# print(davlatlar, x)
# print(davlatlar)


s = [12, 34, 45, 67, 7]
# print(s.index(34))  # (index)ga listdagi yoki tupledagi elementlar nomi beriladi
# print(len(s))
# print(sorted(s))
# print(sorted(s, reverse=True))
# print(s)
# lst = ['python', 'js', 'J', 'C++', 'c', 'C#']
# lst.sort()
# print(lst)
# print(sorted(lst, reverse=True))
# l = [i % 2 == 0 for i in range(120, 1200)]
# print(l)
# l = []
# for i in range(120, 1200):
#     if i % 2 == 0:
#         l.append(i)
# print(l)

# print(sum(s))
# x = min(s)
# f = max(s)
# d = f - x
# print(d)
# print(len(s))
# l = [random.randint(1, 100) for i in range(60)]
# print(l)
# x = l
# print(x[:-20])
# taomlar = ['palov', 'kfc', 'shaurma', 'pizza', 'belistr']
# nonushta = taomlar
# nonushta.pop()
# nonushta.pop()
# nonushta.pop()
# nonushta.pop()
# nonushta.append('gamburger')
# nonushta.append('murskoy kapriz')
# nonushta = tuple(nonushta)
# print(nonushta)

# print('Nonushtaga yeyiladigon ovqatlar:', nonushta)
# print(taomlar)


# Exercise - 1
# a = int(input('Son kiriting: '))
# b = int(input('Son kiriting: '))
# for i in range(a, b - 1, 2):
#     print(i)

#  Exercise - 2
# a = int(input())
# b = int(input())
# for i in range(a - (a + 1) % 2, b - b % 2, -2):
#     print(i, end=' ')


# f = {
#     'ism': 'azim',
#     'yosh': 15,
#     'city': 'Toshkent' 
# }
# print(f"Mani ismim {f['ism'].title()} va man {f['yosh']} daman")
# b = {
#     'name': 'macan',
#     'age': 21,
#     'city': 'moscow'
# }
# print(f"He's name {b['name'].title()} and he lives in the {b['city'].title()} city")

# print(f.fromkeys('yosh', 1))
# x = f.values()
# print(x)
# print(f.get('city', 'None !!!'))
# print(f.items())
# x = f.pop('yosh')
# print(x, f)

# foods = {
#     'a': 'pizza',
#     'b': 'burger',
#     's': 'palov',
#     'o': 'shashlik',
#     'k': 'sandwich'
# }
# print(f"My favourite food is {foods['a'].title()} \n"
#       f"My brother's favourite food is {foods['b'].title()} \n"
#       f"My mum's favourite food is {foods['o'].title()}")

# exams = {
#     'int': 'son',
#     'str': 'harf', 
#     'float': 'kasr',
#     'dict': 'lug\'at',
#     'list': 'ro\'yhat',
# }
# exams['son'] =  'num'
# del exams['int']
# print(exams)
# x = exams.popitem()
# print(exams, x)
# s = exams.setdefault('dict')
# print(exams)
# print(exams)
# print(exams)
# def son_hisobla(son1, son2):
#     product = son1 * son2
#     if product < 1000:
#         return product
#     else:
#         return son1 + son2
# son1 = int(input('1- sonni kiriting: '))
# son2 = int(input('2- sonni kiriting: '))
# num = son_hisobla(son1, son2)
# print(num)


# s = 0
# for i in range(1, 11):
#     s += i
#     print(f"{i}- raqam {i} va uning yig\'indisi :", s)
# print(s)


"""
Berilgan (str) or (int) or (...(list), (tuple)) larni juft indexlarini topish
"""
# word = str(input('Write something: '))
# print(word[0::2])

# word = 'hello azim'
# size = len(word)
# for i in range(0, size - 1, 2):
#     print(f"{i}- indexda: {word[i]}")

# word = input('Enter word ')
# print("Original String:", word)
# x = list(word)
# for i in x[0::2]:
#     print(i)


# def belgilarni_ochir(word, n):
#     print('Original matn:', word)
#     x = word[n:]
#     return x
# print(belgilarni_ochir('miza.kha', 3))
# print(belgilarni_ochir('farhodaka', 6))



"""
Berigan listdagi sonlarning 1- va ohirgi raqamini =ligini tekshirish
"""
# def listni_tekshir(son) ->list:
#     for i in son:
#         for j in son[1:]:
#             if son[i] == son[j]:
#                 return True
#             return False
#     return son
# # l = [10, 20, 30, 40, 10]
# # print(listni_tekshir(l))
# s = [15, 34, 56, 89, 16]
# print(listni_tekshir(s))

# def tekshir(sonlst):
#     son1 = sonlst[0]
#     son2 = sonlst[-1]
#     if son1 == son2:
#         return True
#     return False
# number = [10, 20, 30, 40, 10]
# print(tekshir(number))
# number2 = [75, 25, 35, 45,76]
# print(tekshir(number2))


# def son_chiqar(son):
#     l = []
#     for i in son:
#         if i % 5 == 0:
#             l.append(i)
#     return l
# lst = [10, 20, 33, 46, 55]
# print(son_chiqar(lst))

# str_x = "Emma is good developer. Emma is a writer".split()
# d = {}
# for i in str_x:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)


# def count_emma(statement):
#     count = 0
#     for i in range(len(statement) - 1):
#         count += statement[i: i + 4] == 'Emma'
#     return count

# count = count_emma("Emma is good developer. Emma is a writer")
# print("Emma appeared ", count, "times")

# for i in range(1, 5):
#     for j in range(1, i):
#         print(j, end='')
#     print(i)
    

# for i in range(1, 5):
#     for j in range(6, i):
#         print(j, end='')
#     print(i)


# for i in range(1, 5):
#     for j in range(1, i):
#         print(j, end='')
#     print(i)

# n  = int(input())
# a = n % 10 
# b = n // 10 % 10
# c = n // 100
# s = a + b + c
# print(s)


"""For loop"""
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(i, end=' ')
#     print()


# def myf(num):
#     if num == 0:
#         return num
#     return myf(num - 1)
# x = myf(5)
# print(x)


# for i in range(5, 0, -1):
#     for j in range(1, i):
#         print(j, end=' ')
#     print()



# def exponent(base, exp):
#     return base ** exp
# x = exponent(5, 4)
# print(x)


# lst = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# l = [sum(i) / len(lst) for i in lst]
# print(l)

# a = int(input())
# b = int(input())
# c = int(input())
# if a == b and b == c:
#     print(3)
# elif a == b or b == c or c == a:
#     print(2)
# else :
#     print(0)


# yil = int(input())
# if yil % 4 == 0 and yil % 100 != 0:
#     print('LEAP')
# elif yil % 400 == 0:
#     print('LEAP')
# else:
#     print('COMMON')


# from uuid import uuid4

# class Odamlar:

    # def __init__(self, ism, familiya, ocestva):
        # self.ism = ism
        # self.familiya = familiya
        # self.ocestva = ocestva

    # def getFullInfo(self):
        # return f"Ismi: {self.ism}\nFamiliyasi: {self.familiya}\nOcestvasi: {self.ocestva}"
    
    # def __str__(self):
        # return self.ism
    
# class Student(Odamlar):

    # def __init__(self, ism, familiya, ocestva, kurs):
        # super().__init__(ism, familiya, ocestva)
        # self.__id = uuid4
        # self.__kurs = kurs

    # def add_kurs(self, kurs):
        # if kurs >= 0:
            # self.__kurs += kurs
        # else:
            # print('Qo\'shib Bo\'lmaydi !')
    
    # def getId(self):
        # return self.__id
    
    # def getKurs(self):
        # return self.__kurs
    
    # def __str__(self):
        # return super().__str__()
    
# obj = Odamlar('Ilon', 'Mask', 'Bilmiman')
# ob = Student('Ilon', 'Mask', 'Bilmiman', 6)
# print(ob.add_kurs(3))
# print(obj.getFullInfo())



""" REVIEW """
# a = int(input())
# b = int(input())
# if a < b:
#     for i in range(a, b + 1):
#         print(i)
# elif a > b:
#     for i in range(a, b - 1, - 1):
#         print(i)
# else:
#     print(a)


# s = 0
# for i in range(1, 11):
#     num = int(input(':'))
#     s = s + num
# print(s)


# n = int(input())
# s = 0
# for i in range(n):
#     s += i
#     print(i)
# print(s)


# class User:

#     def __init__(self, full_name, nicname, email):
#         self.full_name = full_name
#         self.nicname = nicname
#         self.email = email

#     def getInfo(self):
#         return f"Foydalanuvchi nicname: {self.nicname}\nFoydalanuvchi ismi: {self.full_name}\nFoydalanuvchi elektron pochtasi: {self.email}"
    
#     def __str__(self):
#         return self.getInfo()
    
# user = User('Azim Qurbonov', 'azimqurbonovv', 'aazimqurbonov63@gmail.com')
# user1 = User('Ali Valiyev', 'valievv', 'valiev@gmail.com')
# print(user)
# print('2 - USER')
# print(user1)



# class Avto:

#     def __init__(self, rang, model, narx):
#         self.rang= rang
#         self.model = model 
#         self.narx = narx
#         self.kilometr = 0

#     def getFullInfo(self):
#         return f"Mashinaning modeli: {self.model}\n\tMashinaning rangi: {self.rang}\n\tMashinaning narxi: {self.narx}$"
    
#     def update_km(self, km):
#         self.kilometr += 1

#     def __str__(self):
#         return self.getFullInfo()

# avt1 = Avto('Qora', 'CLS', 350000)
# avt2 = Avto('Oq', 'G63', 400000)
# avt3 = Avto('Temniy Asfalt', 'W222', 380000)

# class Avtosalon:

#     def __init__(self, salon_nomi, manzil):
#         self.salon_nomi = salon_nomi
#         self.manzil = manzil
#         self.sotuvdagi_avtolar = 0
#         self.avtolar = []

#     def add_avto(self, avto):
#         self.avtolar.append(avto)
#         self.sotuvdagi_avtolar += 1

#     def getInfo(self):
#         s = '\n\t'
#         for i, v in enumerate(self.avtolar, 1):
#             s += f"{i} - mashina:\n\t{v}\n\t"
#         return f"Avtosalon Nomi: {self.salon_nomi}\nAvtosalon Manzili: {self.manzil}\nSotuvdagi Avtomobillar: {s}"
    
#     def __str__(self):
#         return self.getInfo()

# salon = Avtosalon('Kurbanovs', 'Alayskiy')
# salon.add_avto(avt1)    
# salon.add_avto(avt2)    
# salon.add_avto(avt3)
# print(salon)    






