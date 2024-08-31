numbers = []

number = str(input("Enter number :"))
while number != '':
    numbers.append(number)
    number = str(input("Enter number :"))
largest_number = max(numbers)
smallest_number = min(numbers)
print("largest_number : " +largest_number)
print ("smallest_number: " + smallest_number)


