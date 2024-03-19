# """ 1 """
# import random

# my_list = [random.randint(1, 100) for i in range(20)]
# l = sorted(my_list)
# s = l[0]
# d = l[1]
# a = l[2]

# index1 = my_list[0]
# index2 = my_list[0]
# index3 = my_list[0]


# for i in range(len(l)):
#     if l[i] == s:
#         index1 = i
#     if l[i] == d:
#         index2 = i
#     if l[i] == a:
#         index3 = i



# print(l)
# print(f'Eng kichik 3ta sonlar va ularning indexi: \n{s} ning indexi: {index1}\n{d} ning indexi: {index2}\n{a} ning indexi: {index3}')


""" 3 """

# Enter days: 367

# Years: 1
# Weeks: 0
# Days: 2 

# yil = int(input('Son kiriting>>> '))

# y = 365
# h = 7
# q = 0
# d = 0

# for i in range(yil):
#     if yil >= y:
#         q = yil // y
#         e = yil % y
#         hafta = e // h
    

# print(f"{yil} shu kunlarda ichida {q} yil,  {e} kun,  {hafta} hafta bor ")

 

""" 2 """

# with open('input.txt', 'r') as f:
#     l = []
#     for i in f.readlines():
#         l.append(i)
#         print(i)

# l = str(l).split(' ')
# print(len(l)) 

# with open('output.txt', 'w') as f:
#     x = str(len(l))
#     f.write(f"{x}")




""" 4 """
x = 'The quick brown fox jumps over the lazy dog.'

# for i in x:
#     print(i)
