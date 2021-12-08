#Check whether the given year is leap year or not,If year is leap print ‘LEAP YEAR’ elseprint ‘COMMON YEAR’
year = int(input("enter your year"))
if (year % 4) ==0:
    if (year % 100) != 0 :
        if (year % 400)== 0 :
            print ("year,leap year")
        else:
            print ("year , is leap year")
    else:
        print ("year , is leap year")
else:
    print ("year is common year")