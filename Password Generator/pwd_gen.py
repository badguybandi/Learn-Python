import random
import string

def generate_password(min_length, numbers = True, special_characters = True):
    
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if numbers:
        characters += digits

    if special_characters:
        characters += special

    pwd  = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = has_special and meets_criteria

    return pwd

def main():
    
    len_str = input("Enter the minimum length of the password: ")
    while not len_str.isdigit() or int(len_str) < 8:
        print("\nLength must be a digit of  atleast 8")
        len_str = input("Enter the minimum length of the password: ")

    min_length = int(len_str)
    
    num_opt = input("Do you want numbers in the password? (y/n): ")
    while not num_opt.lower() in ["y", "n"]:
        num_opt = input("Do you want numbers in the password? (y/n): ")
    
    spec_opt = input("Do you want special characters in the password? (y/n): ")
    while not spec_opt.lower() in ["y", "n"]:
        spec_opt = input("Do you want special characters in the password? (y/n): ")

    has_number = num_opt.lower() == "y"
    has_special = spec_opt.lower() == "y"
    
    pwd = generate_password(min_length, has_number, has_special)

    print("Password:",pwd)

main()

input()
