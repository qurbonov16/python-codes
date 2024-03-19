import random
# l = []
# for i in range(20):
#     l.append(random.randint(1, 100))
#     if l > 0:
#         print(l)
        

# l = []
# for i in range(20):
#     l.append(random.randint(1.100))
# x = []
# for j in l:
    

# m = int(input("Enter the value of m: "))
# for i in range(1, 1001):
#     if i % 5 == 0: 
#         s = (i // 100) ** 2 
#         q = s // m
#         print("Number:", i, " S:", s, " Q:", q)


#EXERCISE-11
# m = int(input('Enter the value of m:'))
# i = 1
# while i <= 1000:
#     if i % 5 == 0:
#         s = (i // 100) ** 2
#         q = s // m
#         print('Number:', i,"S", s, "Q:", q )
#     i = i + 1
# print(i)


# a = '122 3443'
# l = ['33', '21', 'asd']
# s = ''.join(l)
# print(s)


# my_list = [str(i) for i in range(10, 33)]
# print("||".join(my_list))

# m = ['123', 'abs', '!@#']
# print('^'.join(m))

# for i in range(10):
#     if i % 2 == 0:
#         pass
#     print('Python')


# about = {
#     'name': 'Azim',
#     'age': 16,
#     'adress': 'Muhtar Ashrafiy',
#     'phone_number': '+998946342446'
# }
# about['name'] = 'miza.kha'
# print(about)

# about['email'] = 'azim.qurbonov16@.com'
# print(about)

# print(about.keys())

# print(about.values())

# print(about.copy())

# print(about.items())

# print(type(about.items()))
# for key, value in about.items():
#     print(f"{key} : {value}")

# print(about.pop('name'))
# print(about)


# about.clear()
# print(about)

# x = about.pop('adress')
# print(about, x)


# x = about.popitem()
# y = about.popitem()
# print(about)
# print(x, y)

# names = {
#     'student_1': {'name': 'Azim',
#                   'surname': 'Qurbonov',
#                   'age': 16
#                   },
#     'student_2': {'f_name': 'Ali',
#                     'age': 22
#                     }
# }
# print(na
# about.update(names)
# print(about)

# print(about['name'])
# print(about.get('age1'))
# print(about.get('age2', 'mavjud emas'))

# m = ('asd', 'adsf', 'asfd')
# n = about.fromkeys(0)
# print(n)
# print(about)

# about.setdefault('letter', 'abcd')
# print(about)

# d = {}
# while True:
#     key = input('So\'z kiriting:')
#     value = input('Uz tarjimas:')
#     d[key] = value
#     word = input('Yana so\'z qo\'shishni istaysizmi?:')
#     if word == 'ha' 'yes':
#             continue
#     if word == 'yoq' 'no':
#             break
# print("Siz kiritgan so'zlar:")

# for key, value in d.items():
#         d[key] = value
#         print(f"{key}: {value}")