#Задание выданное на лекции от 18.10.2021
#Напишите программу, которая получает на вход два натуральных числа и определяет количество шагов по разным алгоритмам
a, b = map(int, input("Введите два числа ").split())
b1 = b
a1 = a 
i = 0
i1 = 0
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
    i += 1
if a == 1:
    print("(" + str(a1) + "," + str(b1) + ")" + " - взаимнопростые")
else:
    print("НОД(" + str(a1) + "," + str(b1) + ") = " + str(a))
while b1 != 0:
    a1, b1 = b1, a1 % b1
    i1 += 1
print("Обычный алгоритм: " + str(i))
print("Модифицированный алгоритм: " + str(i1))