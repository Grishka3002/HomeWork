#7.	Напишите функцию Python, которая принимает строку и рассчитывает количество букв верхнего и нижнего регистра.  
a = input("введите строку ")

def bukvischitaem(a):
    mal = 0
    bol = 0
    probel = 0
    for i in range(len(a)):
        if a[i] == a[i].lower() and a[i] != ' ':
            mal = mal + 1
        elif a[i] == a[i].upper() and a[i] != ' ': bol = bol + 1
        else: probel = probel + 1
    print("Больших букв " + str(bol) + ",а маленьких " + str(mal))
bukvischitaem(a)