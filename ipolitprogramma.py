#Задание выданное на лекции от 18.10.2021
#Напишите программу, которая находит количество трёхзначных чисел которые при делении на 15 даёт 11 ,а при делении на 11 9
for i in range(100, 1001):
    if i % 15 == 11 and i % 11 == 9:
        print(i)