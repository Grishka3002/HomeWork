#Задание выданное на лекции от 18.10.2021
#Напишите программу, которая получает на вход натуральное число и определяет простое оно или нет
a = int(input("Введите натуральное число больше 1 "))
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