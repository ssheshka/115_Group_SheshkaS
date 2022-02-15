class Calc:
    def __init__(self):
        self.vvod_chisel()

    def my_summ(self):
        return self.x + self.y

    def my_raznost(self):
        return self.x - self.y

    def my_proizv(self):
        return self.x * self.y

    def my_del(self):
        return self.x / self.y

    def vvod_chisel(self):
        self.x = int(input('Vvedite pervoe chislo = '))
        self.y = int(input('Vvedite vtoroe chislo = '))

while True:
    xxx = input('Vvedite operaciyu  +, -, *, /  ili vvedite 0 for Exit -   ')
    oper = Calc()
    if xxx == "0":
        break
    elif xxx == "+":
        print(oper.my_summ())
    elif xxx == '-':
        print(oper.my_raznost())
    elif xxx == '*':
        print(oper.my_proizv())
    elif xxx == '/':
        print(oper.my_del())
