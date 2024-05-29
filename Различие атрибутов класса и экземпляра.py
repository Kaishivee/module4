class Buiding:
    Total = 0

    def __init__(self):
        Buiding.Total += 1

    def __str__(self):
        return f'Building number {Buiding.Total}'


for i in range(40):
    new_building = Buiding()
    print(new_building)