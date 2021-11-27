#9.	Напишите функцию Python, которая принимает число в качестве параметра и проверяет, является ли число простым или нет.  
a = int(input())

def prostoe(a):
    c = 0
    if a == 2:
        print("Число " + str(a) + " непростое")
    else:
        for i in range(2, a - 1):
            if a % i == 0:
                c += 1
            if c > 0:
                print("Число " + str(a) + " непростое")
                break
        if c == 0:
            print("Число " + str(a) + " простое")
prostoe(a)