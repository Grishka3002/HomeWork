#20.Напишите программу на Python для определения количества локальных переменных, объявленных в функции.  
def fun():
    a = 1
    str = 'GeeksForGeeks'
    b = 3
print(fun.__code__.co_nlocals)