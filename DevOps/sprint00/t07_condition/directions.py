
choise = input("There are 3 signs in front of you. Which one would you like to read? ")
if choise == "right":
    print('The right sign says: "DEAD PEOPLE ONLY"')
elif choise == "left":
    print('The left sign says: "BEWARE!"')
elif choise == "middle":
    print('The middle sign says: "CERTAIN DEATH"')
else:
    print(f'There is no {choise} sign')