#EXERCISE-1
# a = int(input('Write number:'))
# b = int(input('Write number:'))
# c = (a ** 2) + (b ** 2)
# s = (a + b) ** 2
# if c > s:
#     print(f"The sum of the square of {a} and {b} is large")
# else:
#     print(f"The square od the sum of {a} and {b} is large ")

#Exercise-9
# num = int(input('Write number:'))
# if num % 5 == 0:
#     print('This num is divisible by 5')
# else:
#     print('This num is not divisible by 5')

#EXERCISE-12
# a = int(input('Write number:'))
# b = int(input('Write number:'))
# c = (a ** 2) - (b ** 2)
# d = (a -b) ** 2
# if c > d:
#     print('Kvadratlarning ayirmasi katta')
# else:
#     print('Ayirmaning kvadrati katta')

#EXERCISE-9
# num = int(input('Write number:'))
# if num % 2 == 0 and num % 5 == 0:
#     print('Yes, It is divided')
# else:
#     print('No, It is not divided')




#O'RTA BOSQICH
#EXERCISE-15 
# num = int(input('Write number:'))
# c = num % 1000
# d = c // 100 
# print(d)

#EXERCISE-14
# a = int(input('Write number:'))
# b = int(input('Write number:'))
# c = int(input('Write number:'))
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)

#EXERCISE-10
# a = int(input('Write number:'))
# b = int(input('Write number:'))
# c = int(input('Write number:'))
# if a < b and a < c:
#     print('A eng kichigi')
# elif b < a and b < c:
#     print('B eng kichigi')
# else:
#     print('C eng kichigi')

#EXERCISE-12
# a = int(input('Write number:'))
# b = int(input('Write number:'))
# if a % b == 0:
#    print('A B ga bolinadi')
# else:
#    print('A B ga bolinmaydi!!')

#EXERCISE-9
# a = int(input('Write number:'))
# b = int(input('Write number:'))
# c = int(input('Write number:'))
# if (a < b and a > c) or (a > b and a < c):
#     print('a orta')
# elif (b < c and b > a) or (b > c and b < a):
#     print('b orta')
# else:
#     print('c orta')

#EXERCISE-5
# vazn = int(input("Vaznizni kiriting: "))
# boy = int(input("boyizni kiriting: "))
# ideal_vazn = boy - 100
# if vazn == ideal_vazn:
#     print("siz ideal vazndasiz")
# elif vazn > ideal_vazn:
#     n = ideal_vazn - vazn
#     print(f"siz {n} vaznga ozishiz kere")
# elif vazn < ideal_vazn:
#     v = ideal_vazn - vazn
#     print(f"siz {v} kg ga semirishiz kere")

#EXERCISE-6
#O'RTA BOSQICH
#EXERCISE-15 
# num = int(input('Write number:'))
# c = num % 1000
# d = c // 100 
# print(d)

#EXERCISE-14
# a = int(input('Write number:'))
# b = int(input('Write number:'))
# c = int(input('Write number:'))
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)

#EXERCISE-10
# a = int(input('Write number:'))
# b = int(input('Write number:'))
# c = int(input('Write number:'))
# if a < b and a < c:
#     print('A eng kichigi')
# elif b < a and b < c:
#     print('B eng kichigi')
# else:
#     print('C eng kichigi')

#EXERCISE-12
# a = int(input('Write number:'))
# b = int(input('Write number:'))
# if a % b == 0:
#    print('A B ga bolinadi')
# else:
#    print('A B ga bolinmaydi!!')

#EXERCISE-9
# a = int(input('Write number:'))
# b = int(input('Write number:'))
# c = int(input('Write number:'))
# if (a < b and a > c) or (a > b and a < c):
#     print('a orta')
# elif (b < c and b > a) or (b > c and b < a):
#     print('b orta')
# else:
#     print('c orta')

#EXERCISE-5
# vazn = int(input("Vaznizni kiriting: "))
# boy = int(input("boyizni kiriting: "))
# ideal_vazn = boy - 100
# if vazn == ideal_vazn:
#     print("siz ideal vazndasiz")
# elif vazn > ideal_vazn:
#     n = ideal_vazn - vazn
#     print(f"siz {n} vaznga ozishiz kere")
# elif vazn < ideal_vazn:
#     v = ideal_vazn - vazn
#     print(f"siz {v} kg ga semirishiz kere")

#EXERCISE-6
# task = input('What is the Python ?:')
# task2 = input('Who is the founder of Python programming language ?:')
# task3 = input('Why did you chose the Python ?:')
# if ((task == 'programming language') and (task2 == 'guido van rossum')) and (task3 == 'it is easier' or task3 == 'simple'):
#     answer = 'You know more about Python'
# elif (task == 'language that a computer can understand') and (task2 == 'elon musk') and (task3 == 'my dad said' or task3 == 'i want to be like guido'):
#     answer = 'You know little about Python !'
# else:
#     answer = 'You don\'t know much about python !!!'
# print(answer)




# YUQORI BOSQICH
# EXERCISE-7 (A) 
# num = int(input('Write number:'))
# c = num % 100 
# d = (num - c) / 10
# b = d % 10
# s = c + d + b
# print(s)
# if s % 10 == 0:
#     print('True')
# else:
#     print('False')

# EXERCISE-7 (B)
# num = int(input('Write number:'))
# c = num % 100 
# d = (num - c) / 10
# b = d % 10
# s = c + d + b
# print(s)
# if s > 999:
#     print('True')
# else:
#     print('False')

# EXERCISE-8 (A)
# num = int(input('Write number:'))
# b = int(input('Write number:'))
# d = num % 10
# c = ((num - d) % 100) // 10
# e = (num // 100) % 10
# a = (num // 100) // 10
# s = d + c + e + a
# if s > b:
#     print('Uning raqamlari yigindisi katta')
# else:
#     print('Uning raqamlari yigindisi katta emas')

# EXERCISE-8 (B) 
# num = int(input('Write number:'))
# d = num % 10
# c = ((num - d) % 100) // 10
# e = (num // 100) % 10
# a = (num // 100) // 10
# s = d + c + e + a
# if s % 3 == 0:
#     print('3 ga karrali')
# else:
#     print('3 ga karrali emas')

# EXERCISE-10  (A)
# num = int(input('Write number:'))
# d = num % 10
# c = ((num - d) % 100) // 10
# b = (num // 100) % 10
# a = (num // 100) // 10
# s = a + b
# f = c + d
# if s == f:
#     print('Yes, they are equal')
# else:
#     print('No, they are not equal')

# EXERCISE-10  (B)
# num = int(input('Write number:'))
# d = num % 10
# c = ((num - d) % 100) // 10
# b = (num // 100) % 10
# a = (num // 100) // 10
# s = a + b + c + d
# if s % 7 == 0:
#     print('The sum of the numbers is divisible by 7')
# else:
#     print('The sum of the numbers is not divisible by 7')

# EXERCISE-11  (A)
# num = int(input('Write number:'))
# d = num % 10
# c = ((num - d) % 100) // 10
# b = (num // 100) % 10
# a = (num // 100) // 10
# p = a * b * c * d
# if p % 3 == 0:
#     print('The product of numbers is divisible by 3')
# else:
#     print('The product of numbers is not divisible by 3')

# EXERCISE-11  (B)
# num = int(input('Write number:'))
# a = int(input('Write number:'))
# d = num % 10
# c = ((num - d) % 100) // 10
# b = (num // 100) % 10
# f = (num // 100) // 10
# p = f * b * c * d
# if p % a == 0:
#     print('The product of numbers is divisible by a')
# else:
#     print('The product of numbers is not divisible by a')

# EXERCISE-2
# n = int(input('Write number:'))
# if n % 10 == 5 or n // 10 == 5:
#     print('True')
# else:
#     print('False')
