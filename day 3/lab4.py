# enter three integers, print the smallest one
num1 = int (input ("enter first integer : "))
num2 = int (input ("enter second integer :"))
num3 = int (input ("enter third integer:"))
if ( num1 < num2 and num1 < num3 ):
    print ("num1")
elif (num2 < num1 and num2 < num3):
     print ("num2")
else:
    print ("num3")