#11.	Напишите функцию Python, чтобы проверить, является ли число совершенным или нет.
a = int(input())

def sover(a):
    c = 0
    for i in range(1,a):
        if a % i == 0:
            c = c + i
    if a == c:
        print("Да")
    else: 
        print("Нет")
sover(a)