#Write a Python program to select an item randomly from a list.
import random
alpha = ["abc","123","134","asd","ghj","ty","djg"]
a = random.randint(0,len(alpha))
print(f"The Randomly selected item  is: {alpha[a]}")