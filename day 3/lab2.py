A = int(input("enter the marks for subject A"))
B= int(input("enter the marks for subject B"))
C = int (input ("enter the marks for subject C"))
D = int (input ("enter the marks for subject  D"))
total = (A + B+ C + D)
print ("total ")
percentage = (total / 400) * 100
print ("percentage")
if percentage >70 and percentage <= 100 :
    print (" you have scored distinction")
elif percentage >60 and percentage <= 40 :
    print ("  youhave scored first division")
elif percentage >40 and percentage <= 60 :
    print (" you have scored second division")
else:
    print("sorry you have failed")




