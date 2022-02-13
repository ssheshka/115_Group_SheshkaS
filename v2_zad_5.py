# задание 5.
# Написать функцию, которая считает сколько гласных и согласных в строке. Строку вводить с клавиатуры.

def schet(stroka):
    glas = 0
    sogl = 0
    for i in stroka:
        if i.isalpha():
            if i in "уеэоаыяию":
                glas += 1
            else: sogl += 1
    print('Гласных = ', glas)
    print('Согласных = ', sogl)

schet(input('Введите строку : '))


