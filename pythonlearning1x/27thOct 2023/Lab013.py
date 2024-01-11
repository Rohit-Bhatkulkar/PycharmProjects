
#Write a Python program to find the largest number in a list.
# def largestnumber(number):

   Biggestnumber= number[0]

    for num in number:
        if num> Biggestnumber:
            Biggestnumber = num


    return Biggestnumber

 print(largestnumber([1,2,8,10]))

#Write a Python program to find the smallest number in a list.

 def smallestnumber(number):

    smallnumber=number[0]

    for num in number:
        if num < smallnumber:
          smallnumber=num
    return smallnumber

 output=smallestnumber([1,234,0,687632786,3763743])
 print(output)

# Write a Python program to sum all numbers in a list.
 def sumoflist(list1):

    intialsum = 0
     for i in list1:
         intialsum = intialsum + i

     return intialsum
 print(sumoflist([1,2,3]))

# Write a Python program to multiply all numbers in a list.
 def list_mul(Multiply):
    Intial_result = 1
    for i in Multiply:
        Intial_result = Intial_result * i
    return Intial_result

 print(list_mul([1, 2, 3,4]))

#Write a Python program to count the number of strings in a list
#where the string length is 2 or more and the first and last character are the same.

String_List=["a",1,"b","a"]
String=0
for i in String_List:
    if len(String_List)>1 and String_List [0] == String_List [-1]:
        String = String+1

print(String)










