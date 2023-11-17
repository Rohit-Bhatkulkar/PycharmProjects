# Program to find Grade

Score = int(input("Enter your Score \n"))
if (Score >= 90 and Score <= 100):
    print("You got an A grade")

elif (Score >= 80 and Score <= 89):
    print("You got an B grade")

elif (Score >= 70 and Score <= 79):
    print("You got an C grade")

elif (Score >= 60 and Score <= 69):
    print("You got an D grade")

else:
    print("You got an F grade")


#Check Whether a giver year is Leap Year

Year = int(input("Enter Year \n"))
if (Year % 4 == 0 and Year % 100!= 0) or Year % 400 ==0 :
    print(Year , " is Leap Year")

else:
    print("Not a Leap Year")

# Triangle Classifier

Side1 = int(input("Enter Side1 \n"))
Side2 = int(input("Enter Side2 \n"))
Side3 = int(input("Enter Side3 \n"))

if (Side1 == Side2 == Side3):
    print("It is a Equilateral Triangle")

elif (Side1 == Side2 or Side1 == Side3 or Side2 == Side3):
    print("It is a Isoceles Triangle ")

else:
    print("It is a Scalene Triangle ")
