class Car:
    def __init__(self, plate_number, max_speed):
        self.plate_number = plate_number
        self.max_speed = max_speed

class ElectricCar(Car):
    def __init__(self, plate_number, max_speed, battery_capacity):
        self.battery_capacity = battery_capacity
        super().__init__(plate_number, max_speed)


class GasolineCar(Car):
    def __init__(self, plate_number, max_speed, volume):
        self.volume = volume
        super().__init__(plate_number,max_speed)

electric_car = ElectricCar("ABC-15", 180, 52.5 )
gas_car = GasolineCar( "ACD-123",165, 32.3)

distanceE = 3* electric_car.max_speed
print (distanceE)
distanceG = 3 * gas_car.max_speed
print (distanceG)

