# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.

def identify(xxx):
#  если тип объекта кортеж - считаем длинну всех слов
    if isinstance(xxx, tuple):
        n = 0 # длинна всех слов
        for i in xxx:
            s = 0
            if type(i) is str:
                s = len(i)
            n += s
        print('Тип данных - кортеж')
        print('Длинна всех слов = ', n)

#  если тип объекта список - считаем количество чисел и букв
    if isinstance(xxx, list):
        k = 0 # буквы
        n = 0 # числа
        for i in xxx:
            if type(i) is str:
                for j in i:
                    k += 1
            if type(i) is int:
                for j in str(i):
                    n += 1
        print('Тип данных - список')
        print('Количество букв = ', k, 'количество цифр = ', n)


#  если тип объекта число (целое или дробное) - считаем количество нечетных чисел
    if (isinstance(xxx, int)) or (isinstance(xxx, float)):
        my_chislo = str(xxx)
        k = 0
        for i in my_chislo:
            if i.isdigit():
                if (int(i) / 2) != (int(i) // 2):
                    k += 1
        print('тип данных - число')
        print('количество нечетных чисел - ', k)

#  если тип объекта сторока - считаем количество букв
    if isinstance(xxx, str):
        k = 0 # буквы
        for i in xxx:
            if i.isalpha():
                k += 1
        print('тип данных - сторока')
        print('Количество букв = ', k)

# присваиваем объекту данные
kkk = 'kla4ss 24 privet'

identify(kkk)
