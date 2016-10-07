grade = input('Enter your Grade ')
if grade.isdigit():
    ngrade = int(grade)
    if (ngrade > 97  and ngrade <= 100):
        print('A+')
    elif (ngrade > 93  and ngrade <= 96):
        print('A')
    elif (ngrade > 90  and ngrade <= 92):
        print('A-')
    elif (ngrade > 87  and ngrade <= 89):
        print('B+')
    elif (ngrade > 83  and ngrade <= 86):
        print('B')
    elif (ngrade > 80  and ngrade <= 82):
        print('B-')
    elif (ngrade > 77  and ngrade <= 79):
        print('C+')
    elif (ngrade > 73  and ngrade <= 76):
        print('C')
    elif (ngrade > 70  and ngrade <= 72):
        print('C-')
    elif (ngrade > 67  and ngrade <= 69):
        print('D+')
    elif (ngrade > 65  and ngrade <= 66):
        print('D')
    elif (ngrade <= 65):
        print('F')
else:
    if (grade.lower() == "i"):
        print('Incomplete')
    if (grade.lower() == "w"):
        print('withdraw')
