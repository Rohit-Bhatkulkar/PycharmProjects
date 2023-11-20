# # Palindrome

OriginalStr = input("Enter String \n")
newStr=str(OriginalStr[-1::-1])
if OriginalStr == newStr:
    print(OriginalStr, "is a palindrome")
else:
    print(OriginalStr, "is not a palindrome")

# Create a function that calculates the sum of the digits of a positive integer.

def sumofpositiveinteger():
    integer = int(input("Enter a number\n"))
    sum = 0
    for i in range(0, integer + 1):
        sum = sum + integer % 10
        integer = integer // 10
    print(sum)

sumofpositiveinteger()


