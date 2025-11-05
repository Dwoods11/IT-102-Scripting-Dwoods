#By Devante woods

"""
Create a SHA-512 password generator
Generate x amount of password with lengths of chosen and character classes and print plaintext
"""

#Libaries to import run script
import passlib
import string
import secrets

#Create a method to
def prompt_yes_no(msg: str) -> bool:
    while True:
        r = input(f"{msg} [y/n]: ").strip().lower()
        if r in ("yes", "yes"):
            return True
        if r in ("n", "no"):
            return False
        print("please enter answer y or no.")


#Take account of how many passwords to create
count_in = input("How many passwords to generate? (default 5): ").strip()
count = int(count_in) if count_in.isdigit() and int (count_in) > 0 else 5

#Take in the amount of length of passwords user may want
length_in = input("Length of each password (min 8, default 12): ").strip()
length = int(length_in) if length_in.isdigit() and int(length_in) >= 8 else 12

#defining user inputs of what is required of the password
use_upper = prompt_yes_no("Include UPPERCASE LETTERS?")
use_lower = prompt_yes_no("Include lowercase letters?")
use_digits = prompt_yes_no("Include digits?")
use_special = prompt_yes_no("Include Special Cjaracters?")

if not any((use_upper, use_lower, use_digits, use_special)):
    print("No character classess were chosen defaulting to lower class + digits")
    use_lower = True
    use_digits = True

#Create a pool of character, strings, digits, special character
    pool = ""

    if use_upper:
        pool += string.ascii_uppercase
    if use_lower:
        pool += string.ascii_lowercase
    if use_digits:
        pool += string.digits
    if use_special:
        pool += "!@#$%^&*(){}[]\,.<>?"

#Define header for our generated passwords
print("\n==== GENERATED PASSWORDS & SHA512-crypt hashes ====")

for _ in range(count):
    chars = []
    if use_upper:
        chars.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        chars.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        chars.append(secrets.choice(string.ascii_digits))
    if use_special: 
        chars.append(secrets.choice("!@#$%^&*(){}[]\,.<>?"))

    while len(chars) < length:
     chars.append(secrets.choice(pool))

    for i in range(len(chars) - 1, 0, -1):
     j = secrets.randbelow(i+1)
    chars[i], chars[j] = chars[j], chars[i]
    

    password = "".join(chars)
    hashed = sha512.crypt.hash(password) # Produce our hash value


    print(f"password: {password}")
    print(f"sha512 : {hashed}\n")
