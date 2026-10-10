
# DecodeLabs Project 3: Random Password Generator

import random
import string

print("===================================")
print("     RANDOM PASSWORD GENERATOR")
print("===================================")

try:
    length = int(input("Enter password length: "))

    if length < 1:
        print("Please enter a length greater than zero.")
    else:
        characters = string.ascii_letters + string.digits

        password = ''.join(
            random.choice(characters)
            for _ in range(length)
        )

        print("\nYour generated password is:", password)
        print("Password length:", len(password))

except ValueError:
    print("Invalid input! Please enter a whole number.")
