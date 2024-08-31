import random
number = random.randint  (1,10)
guess = int(input("pick a number between 1 and 10 : "))
while guess!=number:


    if guess > number:
        print("to high: ")
    elif guess < number :
        print ("too low: ")
    guess = int(input("pick a number between 1 and 10 : "))

else:
    print (" correct ")









