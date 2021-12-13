#Факториал
a = int(input("Найти факториал числа - "))
def fac(a):
    if a == 0:
        return 1
    return fac(a-1) * a
 
 
print(fac(a))