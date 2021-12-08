#Write a Python program to sum three given integers.However,if two or more values are equal sum will be zero.
num1 = int (input ("enter first number"))
num2 = int (input ("enter second number"))
num3 = int (input ("enter third number"))
if (num1 == num2 and num2 == num3  and num3 == num1 ) :
    print ("the sum of the number is zero ")
else:
    sum= num1 + num2 + num3
    print ("the sum of three integer is :" , sum)
