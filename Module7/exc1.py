seasons = ('winter', 'spring','summer','autumn')

month = int(input("Enter month number: "))
index = month // 3
if month == 12:
    index = 0
print(seasons[index])