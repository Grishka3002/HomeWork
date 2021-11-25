#2.	Напишите функцию Python для суммирования всех чисел в списке
a = list(map(int,input().split(',')))

def sumspisk(a):
    s = 0
    for i in range(len(a)):
        s = s + a[i]
    print(s)
sumspisk(a)