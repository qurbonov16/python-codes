import random
#  EXERCISE-1
# a = int(input('Write number: '))
# b = int(input('Write number: '))
# nums = []
# for i in range(10):
#     num = random.randint(1, 15)
#     nums.append(num)
# print(nums)
# x = []
# for i in nums:
#     if not i in x:
#         x.append(i)
#     if x > nums:
#         print('O\'sish')
# print(x)




#  EXERCISE-2
# l = [random.randint(1, 100) for i in range(10)]       #It's a short solve
# for i in range(10):
#     l.append(random.randint(1, 100))
# print(l)
# max_item = l[0]
# min_item = l[0]
# for i in l:
#     if i > max_item:
#         max_item = i
#     if i < min_item:
#         min_item = i
#     s = max_item + min_item 
# print('Max item:', max_item)
# print('Min item:', min_item)
# print(f"{max_item} va {min_item} sonlarining yig\'indisi {s} soniga teng")


#  EXERCISE-3
# l = []
# s = 0
# for i in range(10):
#     l.append(random.randint(1, 100))
# print(l)
# for i in l:
#     if i > 10 and i < 99:
#         s = s + i
# print(s)


#  EXERCISE-4
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
# for i in range(10):
#     l.append(i)
# print(l)
# juft = []
# toq = []
# for i in l:
#     if i % 2 == 0 and not(i in juft):
#         juft.append(i)
#     if i % 2 != 0 and not(i in toq):
#         toq.append(i)

# print('Juft sonlar:', juft, sum(juft)/len(juft))
# print('Toq sonlar:', toq, sum(toq)/len(toq))


#  EXERCSIE-5
# n = []
# for i in range(10):
#     n.append(random.randint(1, 10))
# print(n)
# true_numbers = []
# false_numbers = []
# for i in n:
#      if i % 2 == 0:
#         print('ROST')
#         true_numbers.append(i)
#      else:
#         print('YOLG\'ON')
#         false_numbers.append(i)
# print(true_numbers)


#  EXERCISE-6
# l = [random.randint(10, 100) for i in range(10)]
# print(l)
# m = []
# s = []
# for i in l:
#     print(i)
#     if i % 3 == 0 and i > 10:
#         m.append(i)
#         print(f"Listmdegi sonla:{m}",f"3 ga bo\'linadigon sonlar: {m}")
#     else:
#         s.append(i)
#         print('Xato')
# print(l)        
# print(m)
# print('xato sonla:', s)



#  EXERCISE-8
# l = [random.randint(1, 100) for i in range(10)]  # short
# l = []
# for i in l:
#     l.append(random.randint(1, 100))
# print(l)
# m = []
# for i in l:
#     if not i in l:
#         print('SONLAR ORASIDA TAKRORLANISH MAVJUD')
#     else:
#         print('SONLAR ORASIDA TAKRORLANISH MAVJUD EMAS')
#         m.append(i)
# print(m)


#  EXERCISE-9 
# l = []
# s = 0
# for i in range(10):
#     l.append(random.randint(-10, 10))
# print(l)
# m = []
# for i in l:
#     if i < 0 and i in l:
#         s = s + i
#         m.append(s)
# print(m)


# EXERCISE-11
# l = []
# for i in range(10):
#     l.append(random.randint(-10, 10))
# print(l)
# max_manfiy = l[0]
# min_musbat = l[0]
# for i in l:
#     if i > max_manfiy and i > 0:
#         max_manfiy = i
#     if i < min_musbat:
#         min_musbat = i
# print(min_musbat)
# print(min_musbat)


#  EXERCISE-13
# l = []
# s = 0
# for i in range(10):
#     l.append(random.randint(1, 9))
# print(l)
# toq = []
# for i in range(len(l)):
#     if i % 2 != 0:
#         s = s + i
#         toq.append(i)
# print(toq, s)
        

#  EXERCISE-14
# l = []
# s = 0
# for i in range(10):
#     l.append(random.randint(1, 9))
# print(l)
# juft_item = []
# for i in range(len(l)):
#     if i % 2 == 0:
#         s = s + i
#         juft_item.append(i)
# print('Juft indexlar:', juft_item)
# print(s)
 

#  EXERCISE-15
# l = []
# for i in range(10):
#     l.append(random.randint(1, 100))
# print(l)
# num = []
# for i in l:
#     if i % 10 == 0:
#         num.append(i)
# print(num)


#  EXERCISE-16
# l = []
# for i in range(10):
#     l.append(random.randint(-10, 11))
# print(l)
# manfiy = []
# for i in l:
#     if i < 0:
#         manfiy.append(i)
# print(manfiy)


#  EXERCISE-17
# a = []
# n = int(input('Son yozing: '))
# for i in range(n):
#     a.append(random.randint(1, 100))
# print(sorted(a))


#  EXERCISE-18
# a = []
# n = int(input('Son kiriting: '))
# for i in range(n):
#     a.append(random.randint(1, 100))
# print(a)
# m = []
# for i in a:
#     if i % 7 == 0:
#         m.append(i)
# print(m)


#  EXERCISE-19
# z = []
# r = []
# for i in range(10):
#     z.append(random.randint(-100, 100))
# print(z)
# m = []
# n = []
# for i in z:
#     if i > 0:
#         m.append(i)
#     if i < 0:
#         n.append(i)
# print(f"Listning musbat elementlari: {m}")
# print(f"Listning manfiy elementlari: {n}")


#  EXERCISE-20
# c = [random.randint(1, 100) for i in range(10)]
# print(c)
# small_number = c[0]
# min_index = []
# for i in c:
#     if i < small_number:
#         small_number = i
# for i in range(len(c)):
#     if c[i] == small_number:
#         min_index.append(i)
# print(f"Eng kichik element: {small_number} va uning indexsi: {min_index}")


#  EXERCISE-21
# b = [random.randint(1, 10) for i in range(5)]
# print(b)
# bigger_number = b[0]
# index = []
# for i in b:
#     if i > bigger_number:
#         bigger_number = i
# for i in range(len(b)):
#     if b[i] == bigger_number:
#         index.append(i)
# print(f"Eng katta element: {bigger_number} va uning tartib raqami: {index}")


#  EXERCISE-22
# a = [random.randint(-10, 10) for i in range(20)]
# print(a)
# minus = []
# index = []
# for i in range(len(a)):
#     if a[i] < 0:
#         minus.append(a[i])
#         index.append(i)
# print('3ta minus son:', minus[:3])
# print('3ta minus sonning indexsi:', index[:3])


#  EXERCISE-23
# x = [random.randint(1, 100) for i in range(15)]
# print(x)
# bigger_number = x[0]
# small_number = x[0]
# bigger_index = []
# small_index = []
# for i in x:
#     if i > bigger_number:
#         bigger_number = i
#     if i < small_number:
#         small_number = i
# for i in range(len(x)):
#     if x[i] == bigger_number :
#         bigger_index.append(i)
#     if x[i] == small_number :
#         small_index.append(i)
# a = []
# a = bigger_number
# bigger_number = small_number
# small_number = a
# l = []
# l = bigger_index
# bigger_index = small_index
# small_index = l
# print(f"Eng katta element: {small_number} va uning tartib raqami: {small_index}")
# print(f"Eng kichik element: {bigger_number} va uning tartib raqami: {bigger_index}")

#  EXERCISE-24
# a = [random.randint(1, 100) for i in range(20)]
# print(a)
# min_number = a[0]
# small_number = []
# index = []
# for i in range(len(a)):
#     if a[i] < min_number:
#         small_number.append(a[i])
#         index.append(i)
# print('Eng kichik 3ta element', small_number[:3])
# print('Eng kichik 3ta elementning indexlari', index[:3])

#  EXERCISE-

