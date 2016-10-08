## Gather the students name
name = input("What is your Full Name ")
## Gather the students’ Current semester number
sem = input("What is your current semester")

## Gather course 1-5 information alternating with courses credit hour 1 information
course1 = input("Course Name 1: ")
coursehr1 = float(input("Course Credit Hour 1: "))
course2 = input("Course Name 2: ")
coursehr2 = float(input("Course Credit Hour 2: "))
course3 = input("Course Name 3: ")
coursehr3 = float(input("Course Credit Hour 3: "))
course4 = input("Course Name 4: ")
coursehr4 = float(input("Course Credit Hour 4 :"))
course5 = input("Course Name 5: ")
coursehr5 = float(input("Course Credit Hour 5: "))

## Asks user for course 1 grade
grade = input('Enter your Grade for Course 1 ')
grade2 = input('Enter your Grade for Course 2 ')
grade3 = input('Enter your Grade for Course 3 ')
grade4 = input('Enter your Grade for Course 4 ')
grade5 = input('Enter your Grade for Course 5 ')
# figure out the letter grade entered
# this also handles incomplete and the withdraw
tgrade = ""
tgrade2 = ""
tgrade3 = ""
tgrade4 = ""
tgrade5 = ""
# A-F grade scipt
if grade.isdigit():
    ngrade = int(grade)
    if (ngrade > 97  and ngrade <= 100):
        tgrade = 'A+'
    elif (ngrade > 93  and ngrade <= 96):
        tgrade = 'A'
    elif (ngrade > 90  and ngrade <= 92):
        tgrade = 'A-'
    elif (ngrade > 87  and ngrade <= 89):
        tgrade = 'B+'
    elif (ngrade > 83  and ngrade <= 86):
        tgrade = 'B'
    elif (ngrade > 80  and ngrade <= 82):
        tgrade = 'B-'
    elif (ngrade > 77  and ngrade <= 79):
        tgrade = 'C+'
    elif (ngrade > 73  and ngrade <= 76):
        tgrade = 'C'
    elif (ngrade > 70  and ngrade <= 72):
        tgrade = 'C-'
    elif (ngrade > 67  and ngrade <= 69):
        tgrade = 'D+'
    elif (ngrade > 65  and ngrade <= 66):
        tgrade = 'D'
    elif (ngrade <= 65):
        tgrade = 'F'
else:
    if (grade.lower() == "i"):
        tgrade = 'Incomplete'
    if (grade.lower() == "w"):
        tgrade = 'withdraw'

#start of grade 2 
if grade2.isdigit():
    ngrade = int(grade2)
    if (ngrade > 97  and ngrade <= 100):
        tgrade2 = 'A+'
    elif (ngrade > 93  and ngrade <= 96):
        tgrade2 = 'A'
    elif (ngrade > 90  and ngrade <= 92):
        tgrade2 = 'A-'
    elif (ngrade > 87  and ngrade <= 89):
        tgrade2 = 'B+'
    elif (ngrade > 83  and ngrade <= 86):
        tgrade2 = 'B'
    elif (ngrade > 80  and ngrade <= 82):
        tgrade2 = 'B-'
    elif (ngrade > 77  and ngrade <= 79):
        tgrade2 = 'C+'
    elif (ngrade > 73  and ngrade <= 76):
        tgrade2 = 'C'
    elif (ngrade > 70  and ngrade <= 72):
        tgrade2 = 'C-'
    elif (ngrade > 67  and ngrade <= 69):
        tgrade2 = 'D+'
    elif (ngrade > 65  and ngrade <= 66):
        tgrade2 = 'D'
    elif (ngrade <= 65):
        tgrade2 = 'F'
else:
    if (grade.lower() == "i"):
        tgrade2 = 'Incomplete'
    if (grade.lower() == "w"):
        tgrade2 = 'withdraw'
#start of grade 3
if grade3.isdigit():
    ngrade = int(grade3)
    if (ngrade > 97  and ngrade <= 100):
        tgrade3 = 'A+'
    elif (ngrade > 93  and ngrade <= 96):
        tgrade3 = 'A'
    elif (ngrade > 90  and ngrade <= 92):
        tgrade3 = 'A-'
    elif (ngrade > 87  and ngrade <= 89):
        tgrade3 = 'B+'
    elif (ngrade > 83  and ngrade <= 86):
        tgrade3 = 'B'
    elif (ngrade > 80  and ngrade <= 82):
        tgrade3 = 'B-'
    elif (ngrade > 77  and ngrade <= 79):
        tgrade3 = 'C+'
    elif (ngrade > 73  and ngrade <= 76):
        tgrade3 = 'C'
    elif (ngrade > 70  and ngrade <= 72):
        tgrade3 = 'C-'
    elif (ngrade > 67  and ngrade <= 69):
        tgrade3 = 'D+'
    elif (ngrade > 65  and ngrade <= 66):
        tgrade3 = 'D'
    elif (ngrade <= 65):
        tgrade3 = 'F'
else:
    if (grade3.lower() == "i"):
        tgrade3 = 'Incomplete'
    if (grade3.lower() == "w"):
        tgrade3 = 'withdraw'
#start of grade 4
if grade4.isdigit():
    ngrade = int(grade4)
    if (ngrade > 97  and ngrade <= 100):
        tgrade4 = 'A+'
    elif (ngrade > 93  and ngrade <= 96):
        tgrade4 = 'A'
    elif (ngrade > 90  and ngrade <= 92):
        tgrade4 = 'A-'
    elif (ngrade > 87  and ngrade <= 89):
        tgrade4 = 'B+'
    elif (ngrade > 83  and ngrade <= 86):
        tgrade4 = 'B'
    elif (ngrade > 80  and ngrade <= 82):
        tgrade4 = 'B-'
    elif (ngrade > 77  and ngrade <= 79):
        tgrade4 = 'C+'
    elif (ngrade > 73  and ngrade <= 76):
        tgrade4 = 'C'
    elif (ngrade > 70  and ngrade <= 72):
        tgrade4 = 'C-'
    elif (ngrade > 67  and ngrade <= 69):
        tgrade4 = 'D+'
    elif (ngrade > 65  and ngrade <= 66):
        tgrade4 = 'D'
    elif (ngrade <= 65):
        tgrade4 = 'F'
else:
    if (grade4.lower() == "i"):
        tgrade4 = 'Incomplete'
    if (grade4.lower() == "w"):
        tgrade4 = 'withdraw'
#start of grade 5
if grade5.isdigit():
    ngrade = int(grade5)
    if (ngrade > 97  and ngrade <= 100):
        tgrade5 = 'A+'
    elif (ngrade > 93  and ngrade <= 96):
        tgrade5 = 'A'
    elif (ngrade > 90  and ngrade <= 92):
        tgrade5 = 'A-'
    elif (ngrade > 87  and ngrade <= 89):
        tgrade5 = 'B+'
    elif (ngrade > 83  and ngrade <= 86):
        tgrade5 = 'B'
    elif (ngrade > 80  and ngrade <= 82):
        tgrade5 = 'B-'
    elif (ngrade > 77  and ngrade <= 79):
        tgrade5 = 'C+'
    elif (ngrade > 73  and ngrade <= 76):
        tgrade5 = 'C'
    elif (ngrade > 70  and ngrade <= 72):
        tgrade5 = 'C-'
    elif (ngrade > 67  and ngrade <= 69):
        tgrade5 = 'D+'
    elif (ngrade > 65  and ngrade <= 66):
        tgrade5 = 'D'
    elif (ngrade <= 65):
        tgrade5 = 'F'
else:
    if (grade5.lower() == "i"):
        tgrade5 = 'Incomplete'
    if (grade5.lower() == "w"):
        tgrade5 = 'withdraw'



## Find the total of courses credit hour by adding courses credit hour1-5 together
total = (coursehr1 + coursehr2 + coursehr3 + coursehr4 + coursehr5)
## Using the number given by the previous calculation divide that number by the amount of classes 
average = (total / 5.0)

## Use the gathered information and list the info in a tabular format
print('Your Name', name)
print('You are in the', sem, 'Semester')

print ("\tHours\t\tName")
print(' '*8, int(coursehr1), ' '*13, course1, ' '*13, tgrade)
print(' '*8, int(coursehr2), ' '*13, course2, ' '*13, tgrade2)
print(' '*8, int(coursehr3), ' '*13, course3, ' '*13, tgrade3)
print(' '*8, int(coursehr4), ' '*13, course4, ' '*13, tgrade4)
print(' '*8, int(coursehr5), ' '*13, course5, ' '*13, tgrade5)
print("---------------------------------------------")
print(' '*8, int(total), ' '*13, int(average))
