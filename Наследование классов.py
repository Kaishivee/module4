class Car:
    price = 1000000

    def __init__(self, name):
        self.name = name

    def __str__(self):
         return 'Машина: {}, Модель: {}, Цена: {}, л.с: {}'.format(
             self.__class__.__name__, self.name, self.price, self.horse_powers)

    def horse_powers(self):
        return horse_powers

class Nissan(Car):
    price = 830000
    horse_powers = 143

class Kia(Car):
    price = 2600000
    horse_powers = 150

nissan_terrano = Nissan(name='Nissan Terrano')
kia_rio = Kia(name='Kia Rio')
print(nissan_terrano)
print(kia_rio)