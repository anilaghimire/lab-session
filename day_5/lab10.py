# write a Python Program that accepts a string and calculate number of digits and letters

word = input("Enter a string: ")
letter_count, space_count, number_count = 0, 0, 0
for character in word:
    if character.isalpha():
        letter_count = letter_count + 1
    if character.isnumeric():
        number_count = number_count + 1
    if character.isspace():
        space_count = space_count + 1
total_count = letter_count + number_count + space_count
special_count = len(word) - total_count
print(
    f"The toal letter,number,spaces,special character in the string ( {word} ) is :  {letter_count},{number_count},{space_count} & {special_count} respectively.")


