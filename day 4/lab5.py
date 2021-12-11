#A student will not be allowed to sit in exam if his/her attendence is less than 75%. input from user Number of classes held
#Number of classes attended.And print percentage of class attended Is student is allowed to sit in exam or not.

a=int(input("number of class held:"))
b=int(input("number of classes attended:"))
percentage= b/a*100
if percentage>=75:
    print("the student is allowed to sit in the exam hall")
else:
    print("the student is not allowed to sit in the exam hall")