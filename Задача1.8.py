#8.	Напишите функцию Python, которая берет список и возвращает новый список с уникальными элементами первого списка.  
a = list(map(int,input().split(',')))

def uniq(a):
    b =[]
    for i in a:
        if i in b:
            continue
        else:
            b.append(i)
    print(b)
uniq(a)