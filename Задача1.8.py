#8.	Напишите функцию Python, которая берет список и возвращает новый список с уникальными элементами первого списка.  
a = list(map(int,input().split(',')))

def uniq(a):
    for i in range(len(a)-1):
        for j in range(i, len(a)):
            if a[i] == a[j]:
                a.pop(i)
    print(a)
uniq(a)