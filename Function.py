import random
l = [random.randint(1, 6) for i in range(5)]
def yigindi(number:int) -> int:
    s = 0
    for i in number:
        s +=i
    return s

print(yigindi(l))


