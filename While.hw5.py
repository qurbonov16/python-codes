"""""
BOSHLANGICH BOSQICH
"""""
#EXERCISE-1
# a = int(input('Write number:'))
# b = int(input('Write number:'))
# n = 0
# while a <= b:
#     print(a)
#     a = a + 1
#     n = n + a
# print(n)

#EXERCISE-2
# a = int(input('Write number:'))
# b = int(input('Write number:'))
# n = 0
# while a >= b:
#     print(a)
#     a = a - 1
#     n = n + a
# print(n)


# EXERCISE-3
# a = int(input('Write number:'))
# n = int(input('Enter degree:'))
# i = 1
# s = 1
# while i <= n:
#     s = s * a
#     i = i + 1
# print(f"Result: {s}")

# EXERCISE-4
# a = int(input('Write number:'))
# n = int(input('Enter degree:'))
# i = 1
# while i <= n:
#     print(f"{a}^{i} = {a ** i}")
#     i = i + 1

#EXERCISE-5
# a = int(input('Write number:'))
# n = int(input('Enter degree:'))
# i = 0
# s = 0
# while i <= n:
#     print(f"{a}^{i} = {a ** i}")
#     s = s + (a ** i)
#     i = i + 1
# print(s)

#EXERCISE-6
# a = int(input('Write number:'))
# i = 1
# s = 0
# while i <= a:
#     s += 1 / i  
#     if i == 9:
#         print(f"1/{i}", end=' = ')
#         print(s)
#     else:
#         print(f"1/{i}", end= ' + ')
#     i = i + 1
# print(s)

#EXERCISE-7
# n = int(input('Write number:'))
# p = 1
# for i in range(1, n):
#     p = p * i
#     print(i)
# print(p)

#EXERCISE-8
# n = int(input('Write number:'))
# p = 1
# for i in range(1, n):
#     p = p * 1 / i
#print('Result:', p)

# EXERCISE-9 
# n = int(input('Write number:'))
# x = int(input('Write degree:'))
# s = 0
# for i in range(1, n):
#     s = s + (x ** i) / i
#     print(i)
# print(s)

#EXERCISE-10
# n = int(input('Write number:'))
# x = int(input('Write degree:'))
# s = 0
# for i in range(1, n):
#     s = s + (pow(-1, i) * pow(x, 2 * i)) + 1 / ((2 * i) + 1)
#     print(i)
# print('Result:', s)

#EXERCISE-11
# x = int(input('Write number:'))
# n = int(input('Write number:'))
# i = 1
# s = 0
# while i <= n:
#     s = s + (pow(-1, i) * pow(x, 2 * i)) / (2 * i)
#     i = i + 2
# print(s)

# EXERCISE-12
# x = int(input('Write number:'))
# n = int(input('Write number:'))
# s = 0
# for i in range(x, n):


#EXERCISE-13
# num = int(input('Write number:'))
# n = 10
# while n <= num:
#     if n % 5 == 0 and n % 2 != 0:
#         print(n)
#     n = n + 1

#EXERCISE-14
# num = int(input('Write number:'))
# n = 11
# while n <= num:
#     print(n ** 2)
#     n = n + 1

#EXERCISE-15
# n = int(input('Write number:'))
# f = 1
# d = 1
# i = 1
# while i <= n:
#     f = f * i
#     d = d * 2
#     print(f, ' = ', d)
#     i = i + 1

# EXERCISE-16
import random
# l = []
# for i in range(10):
#     l.append(random.randint(10, 100))
# max = l[0]
# for i in l:
#     if i > max:
#         max = i
# print("Result:", max)

# EXERCISE-17
# l = []
# for i in range(10):
#     l.append(random.randint(1, 100))
# min = l[0]
# s = 0
# for i in l:
#     if i == min:
#         min = i
#     s = s + i
# print("Result:", min)
# print(s)

# EXERCISE-19
# num = int(input('Write number:'))
# i = 12
# s = 0
# while i <= num:
#     print(i ** 2)
#     s = s + (i ** 2)
#     i = i + 1
# print(s)

#EXERCISE-20
# num = int(input('Write number:'))
# i = 22
# d = 0
# while i <= num:
#     print(i ** 2)
#     d = d - (i ** 2)
#     i = i + 1
# print(d)

#EXERCISE-21
# n = int(input('Write number:'))
# a = int(input('Write number:'))
# d = 0
# for i in range(a, n):
#     print(i ** 2)
#     d = d - (a ** 2) 
# print(d)

#EXERCISE-22
# l = []
# for i in range(10):
#     l.append(random.randint(10, 100))
# min = l[0]
# for i in l:
#     if i < min:
#         min = i
# print(l)
# print('Natija:', min)


#EXERCISE-23
# n = int(input('Write number:'))
# a = int(input('Write number:'))
# for i in range(a, n + 1):
#     print(i ** 2)
# print(a ** n)


#EXERCISE-24
# n = int(input('Write number:'))
# f = 1
# while n > 1:
#     f = f * n
#     n = n - 1
# print(f)

#EXERCISE-25
# n = int(input('Write number:'))
# i = 1
# s = 0
# while i <= n:
#     print(i ** 2)
#     s = s + (i ** 2)
#     i = i + 1
# print(s)

# EXERCISE-26



#EXERCISE-27  A
# n = int(input('Write number:'))
# i = 1
# while i <= n:
#     if i % 5 != 0 and i % 3 == 0:
#         print(i)
#     i = i + 1

#EXERCISE-27  B
# n = int(input('Write number:'))
# i = 1
# while i <= n:
#     if i % 5 == 0 and i % 3 != 0:
#         print(i)
#     i = i + 1

#EXERCISE-28
# n = int(input('Write number:'))
# i = 1
# while i <= n:
#     if i % 5 == 0:
#         print(i)
#     i = i + 1

#EXERCISE-29
# n = int(input('Write number:'))
# i = 0
# while i <= n:
#     if i ** 2 and i ** 0 != 0:
#         print('Yes, it will')
#     else:
#         print("No, it won't")
#     print(i)
#     i = i + 1

#EXERCISE-30
# num = int(input('Write number:'))
# d = num % 10
# c = ((num - d) % 100) // 10
# b = (num // 100) % 10
# print(b, c, d)

#EXERCISE-32
# m = int(input('Write nunber:'))
# n = int(input('Write nunber:'))
# s = 0
# while m <= n:
#     s = s + (m ** 2)
#     print(m ** 2)
#     m = m + 1
# print(s)

#EXERCISE-33
# m = int(input('Write number:'))
# n = int(input('Write number:'))
# s = 0
# while m <= n:
#     if m % 2 != 0:
#         s = s + (m ** 2)
#         print(m ** 2)
#     m = m + 1
# print(s)

#EXERCISE-34
# n = int(input('Write number:'))
# i = int(input('Write number:'))
# p = 1
# while i <= n:
#     if i % 7 == 0 and i % 2 != 0:
#         p = p * i
#         print(i)
#     i = i + 1
# print(p)

#EXERCISE-35
# n = int(input('Write number:'))
# i = int(input('Write number:'))
# s = 0
# while i <= n:
#     if i % 9 == 0 and i > 0:
#         s = s + i
#         print(i)
#     i = i + 1
# print(s)

#EXERCISE-36
# x = 100
# y = 800
# n = int(input("Son kiriting: "))
# s = 0
# for i in range(x, y + 1):
#     if n < i:
#         s += 1
# print(s)

#EXERCISE-40
# t = 0
# for i in range(1, 1000):
#     n = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             n = n + 1
#     if n == 2:
#             t = t + 1
#             print(f'{t} - tub son = {i}')
#     if t == 100:
#         break

#EXERCISE-41
# m = int(input('Write number:'))
# n = int(input('Write number:'))
# p = 1
# while n <= m:
#     if n % 2 == 0:
#         p = p * (n ** 2)
#         print(n ** 2)
#     n = n + 1
# print(p)

#EXERCISE-42
# n = int(input('Write number:'))
# p = 0
# for i in range(1, n):
#     p += i * (i + 1) * 2 * i
# print('Reslut:', p)

# EXERCISE-43
# n = int(input('Write number:'))
# p = 1
# for i in range(1, n):
#     print(pow(i, 3))
#     p = p / i
# print(p)

#EXERCISE-44
# m = int(input('Write number:'))
# n = int(input('Write number:'))
# d = 1
# while n <= m:
#     d = d / n
#     print(pow(n, 2))
#     n = n + 1
# print(d)

#EXERCISE-45
# n = int(input('Write number:'))
# i = int(input('Write number:'))
# s = 0
# while i <= n:
#     if i % 5 == 0 and i < 0:
#         s = s + i
#         print(i)
#     i = i + 1
# print(s)

#EXERCISE-46
# n = int(input('Write number:'))
# i = 1
# s = 0
# while i <= n:
#     if i % 4 == 0 and i < 100:
#         s = s + i
#         print(i)
#     i = i + 1
# print(s)

#EXERCISE-47
# n = int(input('Write number:'))
# i = 1
# d = 1
# while i <= n:
#     d = d / (i ** 2)
#     print(i ** 2)
#     i = i + 1
# print(d)

#EXERCISE-48
# n = int(input('Write number:'))
# i = int(input('Write number:'))
# while i <= n:
#     if i % 2 != 0:
#         print(i)
#     i = i + 1

#EXERCISE-49
# m = int(input('Write number:'))
# n = int(input('Write number:'))
# p = 1
# while n <= m:
#     p = p * (pow(n, 3))
#     print(pow(n, 3))
#     n = n + 1
# print(p)

#EXERCISE-50

#EXERCISE-51
# m = int(input('Write number:'))
# n = int(input('Write number:'))
# p = 1
# while n <= m:
#     if n % 2 != 0:
#         p = p * (n ** 2)
#         print(n ** 2)
#     n = n + 1
# print(p)

#EXERCISE-52
# m = int(input('Write number:'))
# n = int(input('Write number:'))
# s = 0
# while n <= m:
#     if n % 2 == 0:
#         s = s + (n ** 2)
#         print(n ** 2)
#     n = n + 1
# print(s)


"""""
O'RTA BOSQICH
"""""
#EXERCISE-1
# s = 2.54
# for i in range(1, 20):
#     s *= i  
#     print('Result:', s)


#EXERCISE-2
# n = 100
# i = 2
# while i <= n:
#     if i % 5 == 0 and i % 2 == 0:
#         print(i)
#     i = i + 1

#EXERCISE-3
# n = 500
# i = -500
# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     i = i + 1

#EXERCISE-4
# import math
# n = 99
# i = -99
# s = 0
# while i <= n:
#     if i % 2 != 0:
#         s = s + abs(i)
#         print(i)
#     i = i + 1
# print(s)

#EXERCISE-5
# n = int(input('Write number:'))
# i = 0
# while i <= n:
#     if i % 2 != 0:
#         print(i)
#     i = i + 1

#EXERCISE-6
# n = int(input('Write number:'))
# for i in range(n, 0, -1):
#     if n % i == 0:
#         print(i)

#EXERCISE-9


#EXERCISE-16
# m = int(input('Write number:'))
# n = 1
# while n <= m:
#     if n // m == 0:
#         print(n ** 2)
#     n = n + 1

#EXERCISE-20
# m = int(input('Write number:'))
# n = 1
# while n <= m:
#     if n % 2 == 0 and n > 100:
#         n = n % m
#         print(n)
#     n = n + 1

#EXERCISE-11
# n = 120
# i = 1
# m = int(input('Write number:'))
# while i <= n:
#     if i > 99 and i % 5 == 0:
#         m = (i ** 2) / m
#         print(i ** 2)
#         i = i + 1

"""""
FORMS 
"""""

# TASK 
# n = int(input("son kiriting: "))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i == n - 1 or j == n - 1 or i + j == n - 1 or i == j or (i < j < n - i and i < n / 2 - 1) or (i + 1 > j + 1  > n - i   and i > n / 2 - 1):
#             print(" *", end="")
#         else:
#             print("  " , end="")
#     print()

#TASK 2
# a = int(input("Son kiriting:"))
# for i in range(a):
#     for j in range(a):
#         if i == 0 or j == 0 or i == a - 1 or j == a - 1  or a <= i + j <= j + a:
#             print(' * ', end="")
#         else:
#             print('   ', end="")
#     print()

# a = int(input("Son kiriting:"))
# for i in range(a):
#     for j in range(a):
#         if i == 0 or j == 0 or i == a - 1 or j == a - 1 or i == j or a > i + j :
#             print(' * ', end="")
#         else:
#             print('   ', end="")
#     print()
