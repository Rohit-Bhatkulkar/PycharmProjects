# # Task 1
#  = is a Assignment operator
#  == is used to compare two values and return result in boolean.
#
#
# ** operator is the exponential operator which is to riase power of a number
# Example : 2**3 which means 2^3
#
# ^ is ternary Operator reads two integer numbers(in binary format) and gives result in Binary format.

# Task 2

Radius = float(input("Enter Radius of Circle \n"))
print(3.14 * (Radius ** 2))

#  Task 3

num1 = int(input("Enter num 1 : \n "))
num2 = int(input("Enter num 2 : \n "))
if (num1 is num1 > num2):
    print("num1 is greater than num2 \n")

elif (num1 is num1 < num2):
    print("num1 is smaller1 than num2 \n")

else:
    print("num1 is equal to num2 \n")


m1 = int(input("Enter Number 1 \n"))
m2 = int(input("Enter Number 2 \n"))
m3 = int(input("Enter Number 3 \n"))

Max = m1 if (m1 > m2 and m1 > m3) else m2 if ( m2 > m3 and m2 > m1) else m3
print(Max)

a = int(input("Enter the Number \n"))
square = a * a
cube = a*a*a
print("Sqaure of Number is ",square)
print("Cube of Number is ",cube)