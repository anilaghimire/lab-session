#No.1 Write a Python function to find the Max of three numbers
def num(fn,sn,tn):
    if fn>sn and fn > tn:
        print("the max number is :",fn)
    elif sn> fn and sn > tn :
        print("the max num is :",sn)
    else:
        print("the max num is :",tn)
num(1,4,3)

    