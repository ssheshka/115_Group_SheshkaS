#   Функцию которая при заданном целом числе n посчитает n + nn + nnn.

def number(n):
    nn = int(str(n) * 2)
    nnn = int(str(n) * 3)
    s = n + nn + nnn
    return s

print(number(int(input('Введите целое число n = '))))
