from os import system
import random

system('cls')

""" 1 """
# my_list = [random.randint(1, 100) for i in range(20)]

# print(my_list)

# l = sorted(my_list)
# s = l[:3]
# ls1 = []
# lst = [ls1.append(i) for i in range(len(s))]

# print(l)

# print(f"\n{s[0]} - son = {ls1[0]} - o'rinda\n{s[1]} - son = {ls1[1]} - o'rinda\n{s[2]} - son = {ls1[2]} - o'rinda")

""" 2nd solve"""
# for i in range(3):
#     min = my_list[0]
#     index = 0
#     for j in range(len(my_list)):
#         if my_list[j] < min:
#             min = my_list[j]
#             index = j
#     my_list[index] = max(my_list) + 1
#     print(my_list)
#     print(min, index)




""" 2 """
# Enter days: 367

# Years: 1
# Weeks: 0
# Days: 2

# yil_kirit = int(input('Kun kiriting\n>>> '))

# yil = 365
# hafta = 7

# if yil_kirit > yil:
#     y = yil_kirit // yil
#     kun = yil_kirit % yil
#     h = kun // hafta
#     print(f"{yil_kirit} kun ichida: {y} yil  {h} hafta  {kun} kun bor")
# elif yil_kirit < yil:
#     yl = yil_kirit // yil
#     k = yil_kirit % yil
#     haf = k // hafta
#     print(f"{yil_kirit} kun ichida: {yl} yil  {haf} hafta  {k} kun bor")



""" 3 """
# with open('input.txt', 'r') as f:
#     l = []
#     for i in f.readlines():
#         l.append(i)

# l = str(l).split(' ')
# print(len(l)) 

# with open('output.txt', 'w') as f:
#     x = str(len(l))
#     f.write(f"{x}")

""" 2nd solve """
# with open('input.txt', 'r') as f:
#     z = f.read()
#     z = z.split()

# with open('output.txt', 'w') as w:
#     w.write(f"{len(z)}")




""" 4 """
# x = 'The quick brown fox jumps over the lazy dog.'.split()
# l = []
# for i in range(65, 91):
#     l.append(chr(i))
# # for i in x:
# #     for j in i:

# #         print(j)
# print(x)
# print(lst)


# with open('input.txt', 'r') as f:
#     x = f.read().split()
#     l = len(x)
#     with open('output.txt', 'w') as i:
#         l = i.write(f"{l}")

# from random import randint

# my_list = [randint(1, 100) for i in range(20)]
# print(my_list)
# l = sorted(my_list)
# print(l)

# for i, v in enumerate(l[:3]):
#     print(f"{i} : {v}")
    
from os import system

system('cls')

# class Phone:

#     def __init__(self, name, price, year, colour):
#         self.name = name
#         self.price = price
#         self.year = year 
#         self.colour  = colour

#     def getName(self):
#         return self.name
    
#     def setName(self, ism):
#         self.name = ism

#     def getColour(self):
#         return self.colour
    
#     def getFullInfo(self):
#         return f"MODEL: {self.name}\nPRICE: {self.price}$\nYEAR: {self.year}\nCOLOUR: {self.colour}"
    
#     def __str__(self):
#         return self.getFullInfo()
    
# tel = Phone('Samsung S23 ULTRA', 1800, 2023, 'BLACK')
# tel2 = Phone('IPHONE 14 PRO MAX', 1400, 2022, 'BLUE')

# print(tel)
# print(tel2)


# num = int(input('Write a number: '))
# if num % 3 == 0 and num % 4 == 0:
#     print(f"Number {num} divides 3 and 4")
# else:
#     print(f"Number {num} doesn't divide 3 and 4")


# a = int(input('>>'))
# b = int(input('>>'))
# c = int(input('>>'))
# if a <= 0 or b <= 0 or c <= 0:
#     print(0)
# else:
#     print(f"{a}{b}{c}")


# import pyautogui as pg
# import time

# time.sleep(5)
# for i in range(50):
#     pg.write('Ocire')
#     pg.write('\n')




# from turtle import *
# bgcolor('green')
# color('blue')
# begin_fill()
# pensize(3)
# left(50)
# forward(133)
# circle(50,200)
# right(140)
# circle(50,200)
# forward(133)
# end_fill()





