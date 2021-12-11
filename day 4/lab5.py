a=int(input("number of class held:"))
b=int(input("number of classes attended:"))
percentage= b/a*100
if percentage>=75:
    print("the student is allowed to sit in the exam hall")
else:
    print("the student is not allowed to sit in the exam hall")