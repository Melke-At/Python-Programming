print('give mass in talents,pounds and lots')
talents = float(input('first give talents'))
pounds = float(input('then give pounds'))
lots = float(input('then give lots'))
lotsInGrams = 13.3
poundInGrams = 32 * lotsInGrams
talentInGrams = 20 * poundInGrams
mass = talents * talentInGrams + pounds * poundInGrams + lots * lotsInGrams
kg = int(mass//1000)
grams = mass % 1000
print('the weight in modern units;')
print(f'{kg} kilograms and {grams:.2f} grams,')


