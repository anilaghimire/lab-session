#given a positive real number ,print it's fractional part
import math
realnumber = float(input("enter a real number "))
a,b= math.modf (realnumber)
print(b)