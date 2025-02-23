import string
import random

def password_gen(length,complexity) :
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_char = string.punctuation

    char = lowercase
    if (complexity >=2) :
        char += uppercase
    if (complexity >=3) :
        char += digits
    if (complexity >=4) :
        char += special_char
    password = ''.join(random.choice(char) for _ in range(length))
    return password
length = int(input("Enter the length of the password :"))
print(''' Enter 1 for very weak
      Enter 2 for weak
      enter 3 for strong
      enter 4 for very strong ''')
complexity = int(input("Enter your choice : "))
password = password_gen(length,complexity)
print ("Your desired password :", password)
