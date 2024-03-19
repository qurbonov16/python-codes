import random
#  EXERCISE - 1
# def manfiy_sonlar(sonlar:list) ->list:
#     """BU FUNKSIYA LISTDAGI MANFIY SONLARNI LIST KO\'RINISHIDA CHIQARIB BERADI"""
#     manfiy = []
#     for i in sonlar:
#         if i < 0:
#             manfiy.append(i)
#     return manfiy
# l = [random.randint(-10, 10) for i in range(5)]
# print(manfiy_sonlar(l))


#  EXERCISE - 2
# def tub_sonlar(start, end) -> int:
#     """BU FUNKSIYA 2TA SON ORALIG\'GIDAGI TUB SONLARNI LIST TIPIDA CHIQARIB BERADI"""
#     primes = []
#     for num in range(start, end + 1):
#         if num > 1:
#             for i in range(2, num):
#                 if num % i == 0:
#                     break
#             else:
#                 primes.append(num)
#     return primes
# primes = tub_sonlar(1, 20)
# print(primes)

# def title_yasa(string):
#     words = string.split()
#     words1 = [word.capitalize() for word in words]
#     return ' '.join(words1)
# print(title_yasa('hEllo world'))

# def avtohaqida_yasa(model, ismi, narxi, yili:None):
#     avto = {
#         model: 'Amg',
#         ismi: 'Mercedes',
#         narxi: '200.000$',
#         yili: None
#     }
#     return avto
# avto1 = avtohaqida_yasa(model='model', ismi='nomi', narxi='turishi', yili='ciqqan yili')
# print(avto1)


#  EXERCISE-1

def myf(func):#    
    def wrapper(*args, **kwargs):
        x = func(*args, **kwargs)
        l = []
        for i in x:
            if i.isupper():
                l.append(i)
        return l
    return wrapper    
@myf
def title_yasa(string):
    words = string.split()
    words1 = [word.capitalize() for word in words]
    return ' '.join(words1)
print(title_yasa('as zoo icy monkey'))



#  EXERCISE-2
# def uzunlik_sana(uzun):
#     c = 0
#     for i in uzun:
#         c += 1
#     print(len(uzun))
#     return c 
# print(uzunlik_sana('Hello Python I\'m Azim'))
         


#  EXERCISE - 3
# lst = lambda a: sorted(a)
# print(lst(a=('s', 'beny', 'any', 'mercedes', 'bmw')))

# print(lst(('s', 'beny', 'any', 'mercedes', 'bmw')))


#  EXERCISE - 4
# def func1_deco(myf):
#     def wrapper(*args, **kwargs):
#         if args[0] > 0  and args[1] > 0:
#             x = myf(*args, **kwargs)
#             print(f'Son 0 ga bo\'linadi {x}')
#         elif args[0] == 0  or args[1] == 0:
#             print('Sonni 0ga bo\'lib bo\'lmaydi!')
#         return 
#     return wrapper
# @func1_deco
# def func1(num1=int, num2=int):
#     if num1 > 0 and num2 > 0:
#         print(True)
#     else:
#         print(False)
#     return num1 / num2
# print(func1(10, 100))


#  EXERCISE - 5
l = [random.randint(1, 15) for i in range(5)]
print(l)
def sort_yasa(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                tmp = lst[j]
                lst[j] = lst[i]
                lst[i] = tmp
    return lst
print(sort_yasa(l))


# lst = [random.randint(1, 10) for i in range(5)]
# print(lst)
# def juftson_chiqar(son, son1):
#     l = [i for i in range(10) if i % 2 == 0]
#     n = [i for i in range(10) if i % 2 != 0]
#     return l, n
# print(juftson_chiqar(lst, lst))



"""
REKURSIV FUNKSIYA 
"""
# def myf(i=int):
#     if i == 1:
#         return i
#     return i * myf(i - 1)
# x = myf(5)
# print(x)

# def myf(num=int):
#     f = 1
#     for i in range(1, num + 1):
#         f *= i
#     return f
# x = myf(5)
# print(x)


# def son_chiqar(son):
#     if son == 0:
#         return son 
#     print(son)
#     return son_chiqar(son - 1)
# print(son_chiqar(5))


# m = [random.randint(1, 10) for i in range(5)]
# print(m)
# x = list(filter(lambda x: x % 2 == 0, m))
# print(x)






"""
HOMEWORK
"""

#  EXERCISE - 1
# def kvadrat_chiqar(son=int):
#     """Bu funksiya 1dan 'n'gacha bo\'lgan sonlarning kvadratni chiqarib beradi."""
#     if son == 0:
#         return son
#     print(f"{son} * {son} = {pow(son, 2)}")
#     return kvadrat_chiqar(son - 1)
# n = int(input('Son kiriting: '))
# print(kvadrat_chiqar(n))

# print(kvadrat_chiqar.__doc__)



#  EXERCISE - 2
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(l)
# def yigindi_hisobla(son=list):aaaa
#     if len(son) == 0:
#         return 0
#     return son[0] + yigindi_hisobla(son[1:])
# print(yigindi_hisobla(l))


#  EXERCISE - 3
# def ekub_hisobla(son1=int, son2=int):
#     if son2 == 0:
#         return son1
#     return ekub_hisobla(son2, son1 % son2)
# son1 = int(input('1- sonni kiriting: '))
# son2 = int(input('2- sonni kiriting: '))
# msol = ekub_hisobla(son1, son2)
# print(msol)



#  EXERCISE - 4
# nums = (1, 2, 3, 4, 5, 6, 7)
# x = list(map(lambda x: x ** 3, nums))
# print(x)


# EXERCISE - 5
# students = [
#     {'name': 'John', 'age': 18, 'grade': 'A'},
#     {'name': 'Emma', 'age': 19, 'grade': 'B'},
#     {'name': 'Alice', 'age': 17, 'grade': 'A'},
#     {'name': 'Michael', 'age': 20, 'grade': 'C'}
# ]
# x = list(filter(lambda x: x['age']>=18, students))
# print(x)






