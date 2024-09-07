names = []

name = input("Enter first city names or quit by pressing Enter: ")
while len(names) <5:
    names.append(name)
    name = input("Enter city name or quit by pressing Enter: ")

for n in names:
    print( f"{n}")