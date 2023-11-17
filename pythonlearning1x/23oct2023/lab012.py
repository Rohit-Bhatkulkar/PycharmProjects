# Lamba Expression to print cube of a number
cube = lambda a: a ** 3
n = int(input("Enter any Number \n"))
print(cube(n))

# Create a Function with a Parameter which can do x^y
def Param(x, y):
    operation = x ** y
    return operation

Number1 = int(input("Enter any Number 1\n"))
Number2 = int(input("Enter any Number 2\n"))
output = print(Param(Number1, Number2))

# Create a program to print Right Triangle Star Pattern
rows = int(input("Enter Number of Rows : \n"))
for rowNumber in range(1, rows + 1):
    for columnNumber in range(1,rowNumber+1):
        print("*" * rowNumber)
        break

# Create a program Count vowels and consonants in a String
String = input("Enter a word \n")
Vowels = 0
consonants = 0
for i in range(0, len(String)):
    if String[i] == "a" or String[i] == "e" or String[i] == "i" or String[i] == "o" or String[i] == "u":
        Vowels = Vowels + 1

    elif String[i] != "a" or String[i] != "e" or String[i] != "i" or String[i] != "o" or String[i] != "u":
        consonants = consonants + 1

print('Vowels are', Vowels)
print('Consonants are', consonants)
