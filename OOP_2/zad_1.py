
class Human:

    # статические поля (переменные)
    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        # Динамические поля
        # Публичне
        self.name = name
        self.age = age
        # приватные
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Money: {self.__money}')
        print(f'House: {self.__house}')

    @staticmethod
    def default_info():
        print(f'Default Name: {Human.default_name}')
        print(f'Default Age: {Human.default_age}')

    def earn_money(self, amount):
        self.__money += amount
        print(f'Earned {amount} money! Current value: {self.__money}')

if __name__ == "__main__":

    Human.default_info()

    alexander = Human('Sasha', 27)
    alexander.info()

    alexander.earn_money(5000)
    alexander.earn_money(20000)
    alexander.info()
