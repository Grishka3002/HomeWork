#3.	пишите функциНаю Python для умножения всех чисел в списке.  
a = list(map(int,input().split(',')))

def proisspisk(a):
    s = 1
    for i in range(len(a)):
        s = s * a[i]
    print(s)
proisspisk(a)