#Задание выданное на лекции от 18.10.2021
#Напишите программу, которая предлагает ввести число-пароль и не переходит к выполненению пока неведен правильный пароль

import random
i = random.randint(0,9)
a = int(input("Введите пароль "))
while a != i:
    print("Пароль неверный")
    a = int(input("Введите верный пароль "))
print("Секретные данные")