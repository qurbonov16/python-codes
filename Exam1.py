'''
AZIM QURBONOV EXAM 
'''

#  EXERCISE-9
# list1 = [3, 6, 9, 12, 15, 18, 21]
# list2 = [4, 8, 12, 16, 20, 24, 28]
# toq_index = []
# toq_sonlar = []
# juft_index = []
# juft_sonlar = []
# for i in range(len(list1)):
#     if list1[i] % 2 == 0:
#         toq_index.append(i)
# for i in list1:
#     if i % 2 == 0:
#         toq_sonlar.append(i)
# for i in list2:
#     if i % 2 == 0:
#         juft_sonlar.append(i)
# for i in range(len(list2)):
#     # if list2[i] == juft_sonlar:
#     #     juft_index.append(i)
#     if juft_sonlar[i] % 2 == 0:
#         juft_index.append(i)
# print(toq_sonlar)
# print(juft_index, juft_sonlar)


#  EXERCISE-10
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# x1 = set1.difference(set2)
# x2 = set2.difference(set1)
# x3 = x1.union(x2)
# print(x3)

#  EXERCISE-8
# sample_dict = {
#     "name": "Alex",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# print(sample_dict.pop('name'))
# print(sample_dict.pop('salary'))
# print(sample_dict)


#  EXERCISE-7
# a = 'Name', 'Is', 'Jayms'
# print('**'.join(a)) 


#  EXERCISE-1
# my_str ="G'ani g'ildirakni g'ildiratdi."
# print(my_str.count('i'))


#  EXERCISE-2
# my_str ="oq choynakka ko'k qopqoq, ko'k choynakka op qopqoq"
# print(my_str.count('q'))

#  EXERCISE-4
# strA = "uzum beraymi uzum, uzumni ekkan o'zim"
# p = strA.replace('uzum', 'olma')
# print(p)

#  EXERCISE-5
# my_list = [1, 2, 1, 3, 4, 5, 2, 9, 99, 10, 5, 5, 10]
# for i in my_list:
#     if not i in my_list:
#         print(i)




# for i in range(1, 6):
#     for j in range(1, i):
#         print(end='*')
#     print('*')


# n = int(input('Write number: '))
# m = int(input('Write 2nd number: '))
# i = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         print(end='*')
#         j = j + 1
#     print()
#     i = i + 1
# i = 1
# while i <= m:
#     j = m
#     while j >= i:
#         print(end='*')
#         j = j - 1
#     print()
#     i = i + 1



# import random
# l = [random.randint(1, 6) for i in range(5)]
# def ayirma(number:int) -> int:
#     s = 0
#     for i in number:
#         s -= i
#     return s
# print(ayirma(l))

# def kopaytma(number:int) -> int:
#     p = 1
#     for i in number:
#         p *= i
#     return p
# print(kopaytma(l))

# def bolinma(number:int) ->int:
#     d = 1
#     for i in number:
#         if i % 2 == 0:
#             d /= i
#     return d
# print(bolinma(l))

# olma = 'azim qurbonov'
# print(olma.capitalize())
# print(olma.swapcase())
# print(olma.upper())
# print(olma.lower())
# print(olma.title())
# print(olma.replace('azim', 'muhammad'))
# print(olma.count('a'))
# print(olma.find('a'))
# print(olma.index('azim'))
# print(olma.casefold())

# import random
# l = [random.randint(1, 10) for i in range(5)]
# print(l)
# big_num = l[0]
# big_num_index = []
# mid_num = l[0]
# mid_num_index = []
# small_num = l[0]
# small_num_index = []
# for i in l:
#     if i > big_num:
#         big_num = i
#     if i == mid_num and big_num > mid_num > small_num:
#         mid_num = i
#     if i < small_num:
#         small_num = i
# for i in range(len(l)):
#     if l[i] == big_num:
#         big_num_index.append(i)
#     if l[i] == mid_num:
#         mid_num_index.append(i)
#     if l[i] == small_num:
#         small_num_index.append(i)
# print(f"Sonlarning eng kattasi: {big_num} va uning indexsi: {big_num_index}")
# print(f"Sonlarning o\'rtanchasi: {mid_num} va uning indexsi: {mid_num_index}")
# print(f"Sonlarning eng kichikig: {small_num} va uning indexsi: {small_num_index}")



# user = input('TARJIMONDAN FOYDALANISHNI HOHLAYSIZMI(JAVOB HA YOKI YOQ BOLISHI KERAK!)?: ')
# if user == 'ha':
#     print('Davom eting!')
#     for i in range(5):
#         word = input('INGLICHA SOZ KIRITING: ')
#         word2 = input('O\'ZBEKCHASINI KIRITING: ')
#         word3 = input('YANA SO\'Z KIRITISHNI HOHLAYSIZMI?: ')
#         d = []
#         if word3 == 'ha':
#             continue
#         elif word3 == 'yoq':
#             break
#         d.append(word, word2)
#     print(d)
#     print(f"Siz kiritgan so\'zlar: {word}: {word2}")
# elif user == 'yoq':
#     print('To\'xtang !, Siz so\'z kiritmasangiz bundan foydalana olmaysiz!')   

# def write(name:str):
#     '''BU FUNKSIYA USERDAN ISM SORAYDI'''
#     print(f"HELLO MY NAME IS {name}")
# write(name='AZIM')
# print(write.__doc_)

# def enter(ism, tugilgan_yil):
#     '''BU FUNKSIYA USERDAN TUGILGAN YILI VA USERNING ISMINI SORAYDI'''
#     print(f"Assalomu Aleykum: Mening ismim {ism} va men {2023-tugilgan_yil} yoshman")
# enter('Azim', 2007)

# l1 = [12, 34, 45, 56, 67, 68]
# l2 = [23, 34, 5, 6, 7, 8]
# r = l1[1::2] + l2[::2]
# print(r)




""" Exam"""
# Task 1

# def myf():
#     n = int(input("son kiritng:"))
#     if n == 0 :
#         return n
#     myf()
#     print(n)
# myf()


#  Task 2

# def myfuc():
    
#     while True:
#         n = int(input("son kiring: "))
#         s = []
#         if n != 0 :
#             s.append(n)
#         elif n == 0 :
#             s.sort(reverse=True)
#             return(len(s))
            

# print(myfuc())



# with open('Raqamlar.txt', 'w') as f:
#     for i in range(10, 500, 11):
#         f.write(f"\n {i}")
# print('salom')




# class Car: 

#     def __init__(self, name, price):
#         self.name = name 
#         self.price = price 

#     def getName(self):
#         return self.name
    
#     def getFull(self):
#         return f"Nomi: {self.name}\nNarxi: {self.price}"
    
#     def __str__(self):
#         return self.getFull()
    
# class Avto(Car):

#     def __init__(self, name, price, sony):
#         super().__init__(name, price)
#         self.sony = 
#     def getName():
#         return self.sony




# s = 'salom python'
# print(s.center(s))


# l = ['salom', 'pyhton', 1, 23, 'helloworld', 'salom world']
# l.insert(3, 'hello')
# x = l.pop(5)

# l.reverse()
# print(l)



# d = {
#     'name': 'Azim',
#     'age': 16
# }

# x = d.setdefault('yosh')
# print(x)


# s = ['salom', 'python']
# #     print(i)
# x = "yt".join(s)
# print(x)


# print('\U0001F994')





# for i in range(10):
#     i = uuid.uuid4()
#     print(i)