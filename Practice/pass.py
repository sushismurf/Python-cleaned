import random
import string
def generatePassword(length=8):
    while not 8 <= length <= 32:
        print("Password length must be between 8 and 32 characters.")
        length = int(input("How long would you like your password to be? (8-32): "))
    chars = string.ascii_letters + string.digits + "!*?-@"
    password = random.choices(chars, k=length)
    random.shuffle(password)
    return ''.join(password)
while True:
    passLength_input = input("How long would you like your password to be? (8-32): ")
    try:
        length = int(passLength_input)
        break
    except ValueError:
        print("That is not a valid input.")
password = generatePassword(length)
print("Here is your randomly generated", str(length), "character password:", password)
