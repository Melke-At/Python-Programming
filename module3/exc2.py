cabin = str(input('enter type of cabin: '))
if cabin == 'LUX':
    print("upper-deck cabin with a balcony: ")
elif cabin == 'A':
    print("above the car deck, equipped with a window: ")
elif cabin == 'B':
    print("windowless cabin above the car deck: ")
elif cabin == 'C':
     print("windowless cabin below the car deck: ")
else:
    print("Invalid cabin class")