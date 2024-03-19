# m = 'Python'

# for i in m:
#     if i >= chr(90):
#         print(ord(i)) 



a = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
x = (sum(i) / len(i) for i in a)
print(list(x))

