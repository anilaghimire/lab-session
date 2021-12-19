#convert celsius to fahrenheit
temp = input("Enter Temperature in Celcius or Fahrenheite(C/F): ")
if temp == "C":
    temp1 = int(input("Enter Temperature in Celcius: "))
    fahr = ((temp1*9)/5)+32
    print(f"{temp1} in celcius is equal to {fahr} fahrenheite")
elif temp == "F":
    temp2 = int(input("Enter Temperature in Fahrenheite: "))
    C = (5/9) * (temp2 -32)
    print(f"{temp2} in Fahrenheite is equal to {C} Celcius")
else:
    print("You entered Wrong value")