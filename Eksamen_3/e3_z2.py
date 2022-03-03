# Напишите функцию, которая проверяет: является ли слово палиндромом
def reverse(s):
    return s[::-1]

def is_palindrome(s):
    rev = reverse(s)
    # проверка на совпадение 2х строк
    if (s == rev):
        print('Слово палиндром')
    else: print('Слово не палиндром')

# запуск кода
is_palindrome(input('Введите строку :'))
