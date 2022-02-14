class Example:
    default_name = 'Объект'
    name_color = 'зеленый'
    default_speed = 5
    now_speed = 10
    def __init__(self, model, massa):
        self.model = model
        self.massa = massa

    def create(self):
        self.ob = 10
        print(self.ob)

    def summ(self):
        return self.default_name +' ' +self.name_color

    def vozv(self):
        return self.default_speed ** self.now_speed

xxx = Example(4, 2)
print(xxx.default_name)
xxx.create()
print(xxx.summ())
print(xxx.vozv())
