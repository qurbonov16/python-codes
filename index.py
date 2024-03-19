b = []
with open('pwd.txt', 'r') as f:
    for i in f:
        a = i.split(';')
        b.append(a[1].replace('\n', ''))
d = {}
for i in b:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
a = sorted(d.items(), key = lambda item: item[1], reverse=True)
x = a[:11]
for i in x:
    print(f"Eng ko'p ishlatilgan parollardan biri: {i[0]} va u {i[1]} martda ishlatilgan.")


# import os
# import time
# from random import randint
# terminal_length = os.get_terminal_size().columns
# cars = ['\U0001F697','\U0001F3CE', '\U0001F699' ]
# tab = '\t'
# count = terminal_length
# count2 = terminal_length
# count3 = terminal_length
# while True:#'\U0001F699
#     print(tab.expandtabs(count)+'\U0001F699') 
#     print()
#     print(tab.expandtabs(count2)+'\U0001F3CE')
#     print()
#     print(tab.expandtabs(count3)+ '\U0001F697')
#     time.sleep(0.1)
#     count -= randint(1,5)
#     count2 -= randint(1,5)
#     count3 -= randint(1,5)
#     print()
    
#     if count3 < 0 and count2 < 0 and count < 0:
        
#         print('FINISH!!')
#         break
#     print("\033c") 
    


    
   

# import time
# import os
# import random
# a = " "
# b = " "
# c = " "
# emojis = '\U0001f3ce' 
# start = time.time
# counter = 0
# while True:
#     os.system("cls")
#     a += " "* random.randint(0,5)
#     b += " " * random.randint(0,5)
#     c += " " * random.randint(0,5)
#     # time.sleep(1)
#     print(f"{b} {emojis}", '\n', f'{a} {emojis}', "\n", f"{c} {emojis}" )
#     counter += 1
#     if counter == 60:
#         break 
#     time.sleep(0.3)



# import random
# import time
# import os
# def car():
#     v = ['',' ', '  ', '   ', '    ']
#     d = []
#     g = int(input('Wite longivitiy of road: '))
#     x = int(input('Write the number of cars: '))
 

#     for i in range(x):
#         d.append('')

#     while True:
#         counter = 0
#         os.system('cls')
#         for i in range(len(d)):
#             if d[i] >= (' '*g):
#                 print('-'*g, '|')
#                 print(f'{a*(len(d[i])//3)}\U0001F3CD', '\n')
#                 print('-'*g, '|')
#                 counter += 1
#                 continue

            
#             d[i] += random.choice(v)
#             print('-'*g, '|')
#             a = ' - '
#             print(f'{a*(len(d[i])//3)}\U0001F3CD', '\n')
#             print('-'*g, '|')
        

#         if counter == len(d):
#             break

#         time.sleep(0.5)

    

# car()


# import time
# import os
# import random

# color = '\033[46m'
# k = ' '
# y = ' '
# c = ' '
# m = '\U0001F6A3'

# while True:
#     os.system('cls')
#     k += ' ' * random.randint(0, 5)
#     y += ' ' * random.randint(0, 5)
#     c += ' ' * random.randint(0, 5)
#     print(f"{color}{k}{m}", '\n', f'{color}{y}{m}', '\n', f'{color}{c}{m}')
#     if len(k) >= 136 or len(c) >= 136 or len(y) >= 136:
#         print('FINISH \U0001F3C1 ')
#         break
#     time.sleep(0.1)
