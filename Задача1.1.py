#1.	Напишите функцию Python, чтобы найти максимум трех чисел.  
a,b,c = input().split()

def maximum(a,b,c):
    if a > b and a > c:
        m = a
    elif c > a and c > b:
        m = c
    else: m = b
    print(m)
maximum(a, b, c)