#Задание выданное на лекции от 18.10.2021
#Напишите программу, которая получает на вход два натуральных числа и определяет их НОД с помощью модифицированного алгоритма Евклида
a = [64168, 358853, 6365133, 17905514, 549868978]
b = [82678, 691042, 11494962, 23108855, 298294835]
vivod = [] 
print(a)
print(b)   
for i in range(len(a)):
    while b[i] != 0:
        a[i], b[i] = b[i], a[i] % b[i]
    if a[i] == 1:
        vivod.append("Взаимопростые")
    else:
        vivod.append(a[i])
print(vivod)
