import random
def dice_roll():
    roll = 0
    while roll !=6:
        dice = random.randint(1, 6)
        roll = dice
        print(dice)

dice_roll()

