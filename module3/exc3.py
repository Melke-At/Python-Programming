gender = str(input('Enter your gender: '))
hemoglobin = float(input ('enter your hemoglobin count in g/l: '))
if gender == 'male':
  if hemoglobin <= 134:
        print("your hemoglobin is low")
  elif hemoglobin >= 167:
        print("your hemoglobin is high")
  else: print("your hemoglobin value  is normal, 134-167 g/l: ")

if gender == 'female':
    if hemoglobin <= 117:
        print("your hemoglobin is low")
    elif hemoglobin >= 155:
        print("your hemoglobin is high")
    else:
        print("your hemoglobin value  is normal, 117-155 g/l-male: ")



