class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.kilometer_counter = 0

    def set_speed(self, speed):
        if 0 <= speed <= self.max_speed:
            self.current_speed = speed
        else:
            print(f"Speed must be between 0 and {self.max_speed} km/h.")

    def drive(self, hours):
        distance = self.current_speed * hours
        self.kilometer_counter += distance
        print(f"{self.registration_number}: Drove {distance} km. Total kilometers: {self.kilometer_counter} km.")


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity  # in kWh


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume  # in liters


def main():
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    electric_car.set_speed(120)  # Setting speed to 120 km/h
    gasoline_car.set_speed(150)  # Setting speed to 150 km/h

    electric_car.drive(3)
    gasoline_car.drive(3)

    print(f"Electric Car {electric_car.registration_number} has driven {electric_car.kilometer_counter} km.")
    print(f"Gasoline Car {gasoline_car.registration_number} has driven {gasoline_car.kilometer_counter} km.")


if __name__ == "__main__":
    main()
