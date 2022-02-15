#  Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв меньше или равно длине слова, выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.

class Operaciya:
    def __init__(self):
        self.x = ''

    def my_1(self):
        if self.x.isdigit():
            inform = 'Вы ввели число'
            chislo = str(self.x)
            s = 0
            for i in chislo:
                if int(i) // 2 == int(i) / 2:
                    s += int(i)
            proizv = s * len(chislo)
            print(inform)
            print('произведение суммы чётных цифр на длину числа = ', proizv)
        else:
            inform = 'Вы ввели строку'
            gl = 0
            all_gl = []
            sogl = 0
            all_sogl = []
            for i in self.x:
                if i in 'уеэоаыяию':
                    gl += 1
                    all_gl.append(i)
                else:
                    sogl += 1
                    all_sogl.append(i)
            print(inform)
            if gl * sogl <= len(self.x):
                print('Все гласные буквы - ' + ''.join(all_gl))
            else: print('Все согласные буквы - ' + ''.join(all_sogl))

    def my_2(self):
        print('Длинна символов объекта', len(self.x))



parametr = Operaciya()
parametr.x = input('Vvedite dannye : ')
parametr.my_1()
parametr.my_2()
