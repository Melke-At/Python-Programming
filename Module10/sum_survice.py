"""
class Dog:
    created = 0
    def __init__(self, name, birth_year, sound = "woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound
        Dog.created = Dog.created + 1
    def bark(self, times):
        for i in range (times):
            print(self.sound)
        return

dog1 = Dog("Bobi", 2012)
dog2 = Dog("Mechal", 2020, "yip yip yip")
dog1.bark(2)
dog2.bark(3)
print(f"{dog1.name} was born in {dog1.birth_year} and barks {dog1.sound:}" )
print(f"{dog2.name} was born in {dog2.birth_year} and barks {dog2.sound:}" )
print(f"{Dog.created} dogs have been created so far.")
"""
#from Module5.exc4 import names
#from module4.exc3 import number

"""
class Dog:
    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.name + " barks: " + self.sound)
        return

class Hotel:
    def __init__(self):
        self.dogs = []

    def dog_checkin(self, dog):
        self.dogs.append(dog)
        print(dog.name + " checked in")
        return

    def dog_checkout(self, dog):
        self.dogs.remove(dog)
        print(dog.name + " checked out")
        return

    def greet_dogs(self):
        for dog in self.dogs:
            dog.bark(1)

# Main program

dog1 = Dog("Rascal", 2018)
dog2 = Dog("Boi", 2022, "Yip yip yip")
dog3 = Dog("Pappy", 2024)

hotel = Hotel()

hotel.dog_checkin(dog1)
hotel.dog_checkin(dog2)
hotel.dog_checkin(dog3)

hotel.greet_dogs()

hotel.dog_checkout(dog1)

hotel.greet_dogs()
"""
"""
class Car:
    def __init__(self, plate_number, colour):
        self.plate_number = plate_number
        self.colour = colour

class PaintShop:
    def paint(self, car, colour):
        car.colour = colour

paint_shop = PaintShop()
car = Car("ABC-123", "blue")
print("The car is " + car.colour)
paint_shop.paint(car, "red")
print("The car is now " + car.colour)
"""
"""
class Employee:

    total_employees = 0

    def __init__(self, first_name, last_name):
        Employee.total_employees = Employee.total_employees + 1
        self.employee_number = Employee.total_employees
        self.first_name = first_name
        self.last_name = last_name

    def print_information(self):
        print(f"{self.employee_number}: {self.first_name} {self.last_name}")

employees = []
employees.append(Employee("Viivi", "Virta"))
employees.append(Employee("Ahmed", "Habib"))

for e in employees:
    e.print_information()
"""

"""
import requests
import json

keyword = input("Enter keyword: ")

# Request template: https://api.tvmaze.com/search/shows?q=girls
request = "https://api.tvmaze.com/search/shows?q=" + keyword
response = requests.get(request).json()
print(response)

print(json.dumps(response, indent = 2))

for a in response:
    print(a["show"]["name"])
    """

"""
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
Car1 = Vehicle(180, 230000)
car2 = Vehicle(200,12300)

print(Car1.max_speed, Car1.mileage)
print(car2.max_speed, car2.mileage)
"""
"""
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus (Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 230000)
#car2 = Vehicle(200,12300)

print("Vehicle name: ", School_bus.name, "Speed: ", School_bus.max_speed, "Mileage:", School_bus.mileage)
#print(car2.max_speed, car2.mileage)
"""
"""
class Person:
    def person_info(self, name, age):
        print('Inside person class')
        print('Name: ', name, 'Age: ', age)

class Company:
    def company_info(self, company_name, locaton):
        print('Inside company class')
        print('Name: ', company_name, 'location: ', locaton,)

class Employee(Person, Company):
    def Employee_info(self, salary, skill):
        print('Inside Employee class')
        print('salary:', salary, 'skill:', skill)

emp = Employee()

emp.person_info('Jessa', 28)
emp.company_info('Google', 'Atlanta')
emp.Employee_info(12000, 'Machine Learning')
"""
"""
class Publication:

    def __init__(self, name):
        self.name = name

    def print_information (self):
        print("Name",self.name)

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        super().print_information()
        print("Author", self.author, f"({self.page_count} pages)")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor


    def print_information(self):
        super().print_information()
        print("chief editor", self.chief_editor)

publications = []
publications.append(Magazine("Donald Duck", "Aki Hyyppa"))
publications.append(Book("Compartment No.6", "Rosa Liksom",192))

for pubs in publications:
    pubs.print_information()
    """














