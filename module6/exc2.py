import random

def dice_roll(x):
    roll = 0
    while roll !=x:
        dice = random.randint(1, x)
        roll = dice
        print(roll)
dice_roll(21)




