number = int(input("Enter an integer: "))

isprime = 'not'

if number != 1:
    isprime = ' '
    for i in range(2,number):

        if number % i == 0:
            isprime = 'not'
            break

print(f"{number} is{isprime} a prime number: ")


