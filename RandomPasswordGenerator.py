# Prompting user to enter their desired password length and validating the input
while True:
    try:
        length = int(input("Please enter your desired length for your password: "))
        if length > 0:
            break # Valid length number entered, exit loop
        else:
            print("Please enter a positive length.")
    except ValueError:
        print("Invalid length entered. Please try again.")

# Initialising password_char as an empty string to store selected characters
password_char = ""

# Ask the user to select which character type (letters, digits, special characters)
while not password_char:
    include_letters = input("Include letters (yes/no)? ").strip().lower() == 'yes'
    include_digits = input("Include digits (yes/no)? ").strip().lower() == 'yes'
    include_special_char = input("Include special characters (yes/no)? ").strip().lower() == 'yes'

    import string
    letters = string.ascii_letters # Includes both lowercase and uppercase letters
    digits = string.digits # Include digits 0-9
    special_char = string.punctuation # Includes special characters such as !, @, #, $, %, ^, &, *

# Adding the character sets to password_char based on the user's choice
    if include_letters:
        password_char += letters
    if include_digits:
        password_char += digits
    if include_special_char:
        password_char += special_char

    if not password_char:
        print("You have to choose on of the above types to generate your password.")

# Generating the password through random selection of characters from the chosen charater set
import random
password = ''.join(random.choices(password_char, k = length))
print(f"Your password is: {password}")