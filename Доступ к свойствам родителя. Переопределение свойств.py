class Vehicle:
    __COLOR_VARIANTS = ['red', 'blue', 'pink', 'orange', 'black']

    def __init__(self, owner, __model, __engine_power, __color):
        super().__init__()
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model()),
        print(self.get_horsepower())
        print(self.get_color())
        print("Владелец:", self.owner)

    def set_color(self, new_color=str):
        for _ in self.__COLOR_VARIANTS:
            if new_color.casefold() in self.__COLOR_VARIANTS:
                self.__color = new_color.lower()
            else:
                return f'Нельзя сменить цвет на {new_color}'


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


veh1 = Vehicle('Fedos', 'Toyota Mark II', 500, 'blue')
veh1.print_info()
print(veh1.set_color('grey'))
veh1.set_color('BLACK')
veh1.print_info()
