#12.	Напишите функцию Python, которая проверяет, является ли переданная строка палиндромом или нет.  
a = input()

def reverse(a): 
    return a[::-1] 
  
def is_palindrome(a): 
    rev = reverse(a) 
    if (a == rev): 
        print("Да")
    else: print('Нет')

is_palindrome(a)