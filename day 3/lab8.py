#given n-digit number,find the sum of  it
number = int (input ("enter a number"))
sumofdigit = 0
for digit in str (number):
    sumofdigit = int(digit)
print(sumofdigit)