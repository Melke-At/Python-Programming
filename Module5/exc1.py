import random

number_of_dice =int(input("how many dice you want to roll "))
total_sum = 0
for n in range(number_of_dice):
        roll = random.randint(1,6)
        total_sum += roll
        print(f"rolled, {roll}")
print(f"the total sum of the dice rolls is: {total_sum} ")


