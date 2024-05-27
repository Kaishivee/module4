class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


first_floor = Building(1, 'Первый этаж')
second_floor = Building(2, 'Второй этаж')

print(first_floor == second_floor)        #False

first_floor = Building(1, 'Первый этаж')
other_first_floor = Building(1, 'Первый этаж')

print(first_floor == other_first_floor)         #True
