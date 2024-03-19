list1 = [5, 10, 15, 20, 25, 50, 20] 

# for i in list1:
#     if i in list1 and i == 20:
#         i = 200
#         break
#     print(False)
# print(list1)

# list1 = [5, 20, 15, 20, 25, 50, 20]
# print(list1)
# for i in range(len(list1)):
#     if list1[i] == 20:
#         list1[i] = 200
#         print(list1[i])
#         print(list1)
#         break
#     print(False)

# list1 = [5, 20, 15, 20, 25, 50, 20]
# print(list1)
# l = []
# for i in list1:
#     if i == 20:
#         list1.remove(i)
#         l.append(i)

# print(list1)
# print(l)



# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# list2.reverse()

# print(list(zip(list1, list2)))

import random

# l = [random.randint(-10, 10) for i in range(10)]  
# print(l)

# max_item_manfiy = []
# min_item_musbat = []

# for i in l:
#     if i < 0:
#         max_item_manfiy.append(i)
#     if i > 0:
#         min_item_musbat.append(i)

# min_musbat = min_item_musbat[0]
# for i in min_item_musbat:
#     if i < min_musbat:
#         min_musbat = i

# max_manfiy = max_item_manfiy[0]
# for i in max_item_manfiy:
#     if i > max_manfiy:
#         max_manfiy = i




# print('Eng kotta MANFIY element:', max_manfiy)
# print('Eng kichik MUSBAT element:', min_musbat)


#  0 dan kotta bosa MUSBAT, bomasam MANFIY

# numbers = [random.randint(-10, 10) for i in range(10)]

# max_manfiy = None
# min_musbat = None

# for num in numbers:
#     if num < 0:
#         if max_manfiy is None or num > max_manfiy:
#             max_manfiy = num
#     elif num > 0:
#         if min_musbat is None or num < min_musbat:
#             min_musbat = num

# print("Eng katta manfiy element:", max_manfiy)
# print("Eng kichik musbat element:", min_musbat)



# SORT FUNCTION 
lst = [random.randint(1, 15) for i in range(5)]
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            tmp = lst[j]
            lst[j] = lst[i]
            lst[i] = tmp
print(lst)
