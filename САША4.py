# Функция, которая возвращает натуральный логарифм
import math
b = list(map(float, input().split(',')))
def a(b):
    for i in range(len(b)):
        if b[i] == 0 or b[i] < 0:
            b[i] = None
            continue
        b[i] = math.log(b[i])
    print(b)
a(b)
        