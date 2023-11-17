#Fibonacci Series
a , b = 0, 1
while a < 10:
    print(a,"\n", end='')
    a ,b = b, a+b

#factorial
Num = int(input("Enter number \n"))
fact = 1
for i in range(1, Num +1):
    fact=fact*i

print(fact)

# Example using break to exit a loop when i == 51 while printing the values from 1 to 100
for i in range(0, 100):
    if (i == 50):
        print(i)
        break

