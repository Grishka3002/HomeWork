#4.	Напишите программу на Python для обращения строки.  
a = str(input())

def perevernul(a):
    b = list(a)
    for i in range(len(a)//2):
        c = b[i]
        b[i] = b[len(a)-i-1]
        b[len(a)-i-1] = c
    print(''.join(b))
perevernul(a)