import random
# son = int(input())
# num = int(input())
# print(son * num)


# son = int(input())
# if son > 10 and son < 99:
    # print(True)
# else:
    # print(False)
""" 2chi reshenie"""
# print(son > 10 and son <= 99)


# son = int(input('3 xonali son kiriting !: '))
# if son > 99  and son < 1000:
    # print(son % 10)
# else:
    # print('3 xonali son kiritishingiz kerak !!!')
# print((son > 99 and son < 1000), son % 10)


# son = int(input())
# if son % 2 == 0:
    # print(f"{son} soni juft")
# else:
    # print(f"{son} soni toq")


# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i):
#         print(j, end=' ')
#     print(i)
# for i in range(n, 0, -1):
#     for j in range(1, i):
#         print(j, end=' ')
#     print()


# lst = [1, 2, 3, 4, 5, 6, 123]
# max_son = lst[0]
# for i in lst:
#     if i > max_son:
#         max_son = i
# print(max_son)


# lst = [1, 2, 3, 4, 5, 6]
# c = 0
# s = 0
# for i in lst:
#     s = s + i
#     c = c + 1 
# print(s / c)


# l = [12, 23, 45, 67, 78]
# r = [i // 10 for i in l]
# print(r)


# m = [random.randint(1, 100) for i in range(20)]
# print(m)
# l = []
# for i in range(len(m)):
#     while True:
#         if i % 2 == 0 and m[i] % 2 == 0:
#             l.append(i)
#         break
# print(l)

# my_list = ['_aziz_', '_sarvar_', '_ali_', '_islom_', '_maruf_']
# l = []
# for i in my_list:
#     x = i.strip('_')
#     l.append(x)
# print(l)


"""
Homeworks !
"""
#  EXERCISE   1
# a = int(input('1- sonni kiriting: '))
# b = int(input('2- sonni kiriting: '))
# c = a * b
# print(f"{a} * {b} = {c}")


#  EXERCISE   2
# print('Name', 'Is', 'James', sep='**')


#  EXERCISE   3
# num = 8
# print('%o' % num)


#  EXERCISE   4
# num = 458.541315
# print('%.2f' % num)


#  EXERCISE   5
# sonlar = []
# for i in range(1, 6):
#     print('Kiritlgan raqam >>>', i)
#     son = float(input('Son kiriting: '))
#     sonlar.append(float(son))
# print(sonlar)

#  EXERCISE   6



#  EXERCISE   7
# name1, name2, name3 = input('Ism kiriting: ').title().split()
# print('1- ism:', name1)
# print('2- ism:', name2)
# print('3- ism:', name3)


#  EXERCISE   8
# summa = 1000
# narsa = 3
# narx = 450
# print(f"Manda {summa}$ bor va man {narx}$ dan {3} dona futbolka ololiyman !")


#  EXERCISE   9


#  EXERCISE   10
# i = 1
# while i <= 10:
#     print(i)
#     i += 1


#  EXERCISE    11
# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print(j, end=' ')
#         j += 1
#     print()
#     i += 1

""" Solve 2 """
# for i in range(1, 6):
#     for j in range(1, i):
#         print(j, end=' ')
#     print(i)


#  EXERCISE   12
# i = 1
# s = 0
# while i <= 10:
#     s += i
#     i += 1
# print(s)


#  EXERCISE   13
# n = 2
# for i in range(1, 11):
#     print(i * n)


#  EXERCISE   14
# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i % 5 == 0:
#         print(i)


#  EXERCISE   15
# num = int(input())
# c = 0
# while num != 0:
#     num = num // 10
#     c += 1
# print(f'Sonining uzunligi: {c}')


#  EXERCISE   16
# for i in range(6, 0, -1):
#     for j in range(1, i):
#         print(j, end=' ')
#     print()


#  EXERCISE   17
# l = [10, 20, 30, 40, 50]
# n = reversed(l)
# for i in n:
#     print(i)


#  EXERCISE   18
# for i in range(-10, 0):
#     print(i)


#  EXERCISE   19
# for i in range(5):
#     print(i)
# else:
#     print('Done !')



#  EXERCISE   20
# n = int(input())
# f = 1
# for i in range(1, n + 1):
#     f = f * i
# print(f"{n} sonining faktoriali: {f}")



#   EXERCISE   21
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# lst = []
# for i in my_list[1::2]:
#     lst.append(i)
# print(lst)


#  EXERCISE   22
# n = int(input('Son kiriting: '))
# for i in range(1, n + 1):
#     print(f"{i} ** 3 = {i ** 3}")


#  EXERCISE   23
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i):
#         print('*', end=' ')
#     print('*')
# for i in range(n, 0, -1):
#     for j in range(1, i):
#         print('*', end=' ')
#     print()


""" STRING """
#  EXERCISE   24
# str1 = 'James'
# print(str1[0::2])

# str2 = "JaSonAy"
# print(str2[2:5])

# str3 = "JhonDipPeta"
# print(str3[4:7])


#  EXERCISE   25
# s1 = "Ault"
# s2 = "Kelly"
# s3 = s1 + s2
# print(s3)


#  EXERCISE   26
# str1 = "Azim14@#"
# b = 0
# r = 0
# s = 0
# for i in str1:
#     if i.isalpha():
#         b += 1
#     elif i.isdigit():
#         r += 1
#     else:
#         s += 1

# print(f"Belgilar: {b}, Raqamlar: {r}, Simbollar: {s}")



#  EXERCISE   27
# str1 = "Apple"
# d = {}
# for i in str1:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)


#  EXERCISE   28
# str1 = "PYnative"
# print(str1[::-1])


#   EXERCISE   29
# str1 = 'Emma-is-a-data-scientist'.split('-')
# for i in str1:
#     print(i)


#  EXERCISE   30
# str1 = "/*Jon is @developer & musician"
# l = []
# p = []
# for i in str1:
#     if i.isalpha():
#         l.append(i)
#     else:
#         p.append(i)

# print(type(p))


#  EXERCISE   31
# str1 = 'I am 25 years and 10 months old'
# s = []
# for i in str1:
#     if i.isdigit():
#         s.append(i)
# print(s)


#  EXERCISE   32
# str1 = '/*Jon is @developer & musician!!'
# s = str1
# l = []
# for i in s:
#     if i.isalpha():
#         pass
#     else:
#         l.append(i)
# print(l)


""" List """
#  EXERCISE   33
# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1)


#  EXERCISE   34
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# lst = [i + j for i, j in zip(list1, list2)]
# print(lst)


#  EXERCISE   35
# numbers = [1, 2, 3, 4, 5, 6, 7]
# l = []
# for i in numbers:
#     l.append(i ** 2)
# print(l)


#  EXERCISE   36
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# lst = [i + j for i in list1 for j in list1]
# print(lst)


#  EXERCISE   37
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for i, j in zip(list1, list2[::-1]):
#     print(i, j)


#  EXERCISE   38
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# lst = list(filter(list1.remove(""), list1))
# print(lst)


#  EXERCISE   39
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]



""" Dict """
#  EXERCISE   40
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# for i, j in zip(keys, values):
#     print(i, j)


#  EXERCISE   41
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(sampleDict['class']['student']['marks']['history']) 


#  EXERCISE   42
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# print(defaults.fromkeys(employees, defaults))


#  EXERCISE   43
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
# keys = ["name", "salary"]
# x = {k: sample_dict[k] for k in keys}
# print(x)


#  EXERCISE   44
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# keys = ["name", "salary"]
# for k in keys:
#     sample_dict.pop(k)
# print(sample_dict)


#  EXERCISE   45
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# d = sample_dict.values()
# for i in sample_dict.values():
#     if i in sample_dict.values():
#         print(True)
#     else:
#         print(False)
#     print(i)
    

#  EXERCISE   46
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# sample_dict['location'] = sample_dict.pop('city')
# print(sample_dict)


#  EXERCISE   47
    # sample_dict = {
    #   'Physics': 82,
    #   'Math': 65,
    #   'history': 75
    # }
    # print(min(sample_dict))


#  EXERCISE   48
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# sample_dict['emp3']['salary'] = 8500
# print(sample_dict)


""" Function """
#  EXERCISE   49
# def yoz(son, harf):
#     print(son, harf)
# print(yoz(12, 'Salom'))


#  EXERCISE   50
# def son_yoz(*args):
#     for i in args:
#         print(i)
# son_yoz(10, 20)
# son_yoz(30, 40, 50)
# son_yoz(60, 70, 80)


#  EXERCISE   51
# def hisobla(a, b):
#     s = a - b
#     d = a + b
#     return s, d
# print(hisobla(36, 9))


#  EXERCISE   52
# def func_yasa(ism, oylik=10000):
#     print(f'Ism: {ism}. Oylik: {oylik}')
# func_yasa('Azim', 12000)
# func_yasa('Ben', 20000)


#  EXERCISE   53
# def hisobla(a):
#     if a == 0:
#         return a 
#     else:
#         return a + hisobla(a - 1)
# print(hisobla(10))

    


#  EXERCISE   54
# def myf(name, age):
#     print(f"Ism: {name.title()}. Yosh: {age}")
# myf('ben', 16)

# func = myf
# func('sabina', 15)


#  EXERCISE   55
# def juft_son_top(son):
#     l = []
#     for i in range(4, son + 1):
#         if i %  2 == 0:
#             l.append(i)
#     print(l)
# juft_son_top(30)



#  EXERCISE   56
# def kotta_son_top(son):
#     max_item = son[0]
#     for i in son:
#         if i > max_item:
#             max_item = i
#     print(max_item)
# lst = [random.randint(1, 10) for i in range(5)]
# print(lst)
# kotta_son_top(lst)


""" Set """
#  EXERCISE   57
# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]
# sample_set.update(sample_list)
# print(sample_set)


#  EXERCISE   58
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set1.intersection_update(set2)
# print(set1)


#  EXERCISE   59
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.union(set2))


#  EXERCISE   60
# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
# set1.difference_update(set2)
# print(set1)


#  EXERCISE   61
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.symmetric_difference(set2))


#  EXERCISE   62
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
# if set1.isdisjoint(set2):
#     print(False)
# else:
#     print(set1.intersection(set2))


#  EXERCISE   63
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set1.symmetric_difference_update(set2)
# print(set1)


#  EXERCISE   64
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set1.intersection_update(set2)
# print(set1)


""" Tuple """
#  EXERCISE   65
# tuple1 = (10, 20, 30, 40, 50)
# print(tuple1[::-1])


#  EXERCISE   66
# tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# f = ()
# for i in tuple1[1]:
#     if i == 20:
#         f = i
# print(f)

""" Solve """
# tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# print(tuple1[1][1])


#  EXERCISE  67
# t = (50)
# print(t)


#  EXERCISE  68
# tuple1 = (10, 20, 30, 40)
# a, b, c, t = tuple1
# print(a)


#  EXERCISE  69
# tuple1 = (11, 22)
# tuple2 = (99, 88)
# s = tuple1
# tuple1 = tuple2
# tuple2 = s
# print(tuple2)


#  EXERCISE  70
# tuple1 = (11, 22  , 33, 44, 55, 66)
# f = []
# for i in tuple1:
#     if i == 44 or i == 55:
#         f.append(i)
#     print(i)
# f = tuple(f)
# print(f)


#  EXERCISE  71
# tuple1 = (11, [22, 33], 44, 55)
# tuple1[1][0] = 222
# print(tuple1)


#  EXERCISE  72
# tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
# t = tuple(sorted(list(tuple1), key=lambda x: x[1]))
# print(t)


#  EXERCISE  73
# n = (input('Rim raqamlari kiriting: ')).split()
# d = {
#     'I' : 1,
#     'V' : 5,
#     'X' : 10,
#     'L' : 50,
#     'C' : 100,
#     'D' : 500,
#     'M' : 1000
# }
# for i in d:
#     if d[i] == n:
#         print(i)


