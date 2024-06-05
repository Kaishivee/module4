class Vehicle:
    vehicle_type = "none"

    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'Марка: {}, Тип кузова: {}, Цена: {}, л.с: {}'.format(
            self.__class__.__name__, self.vehicle_type, self.price, self.horse_powers())


class Car:
    price = 1000000

    def horse_powers(self):
        return horse_powers


class Nissan(Car, Vehicle):
    price = 1867000
    vehicle_type = 'Внедорожник 5 дв.'

    def horse_powers(self):
        horse_powers = 114
        return horse_powers


nissan_terrano = Nissan()
print(nissan_terrano)
print(nissan_terrano.vehicle_type, nissan_terrano.price)