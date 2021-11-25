#6.	Напишите функцию Python, чтобы проверить, находится ли число в заданном диапазоне.  
a = int(input("Число "))
b,c = list(map(int,input("Диапозон от ... до ... ").split()))

def diaposon(a,b,c):
    if c > a and a > b:
        print("Да")
    else: print("Нет")
diaposon(a,b,c)
