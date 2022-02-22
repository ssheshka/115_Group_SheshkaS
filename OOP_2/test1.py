# Родительский класс
class Phone:

    # Инициализатор - создание объекта
    def __init__(self):
        self.is_on = False

    # Включение телефона
    def turn_on(self):
        self.is_on = True

    # Если телефон включен - делаем звонок
    def call(self):
        if self.is_on:
            print('Телефон звонит...')

# унаследованный класс

class MobilePhone(Phone):
    # Новое свойство
    def __init__(self):
        super().__init__()
        self.battary = 0

# Заряжаем телефон
def charge(self, num):
    self.battary = num
    print(f'Зарядка телефона .... {self.battary}%')

my_mobile_phone = MobilePhone()
dir(my_mobile_phone)
#my_mobile_phone.charge(5)
charge(my_mobile_phone, int(input('Введите велечину заряда = ')))

