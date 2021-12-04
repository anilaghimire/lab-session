#student take k apples and distrubte them evenly
#how many apple will each student get and how many will remain in the basket
N= int(input("enter the number of the student:"))
K= int(input("enter the number of apple in the basket:"))
student = K / N
remaining = K % N
print ("the number of apple for each student is :", student)
print("the number of remaining apple in the basket is :", remaining)
