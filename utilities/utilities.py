import string
import random

class PasswordGen():
    # Asks for a website name from the user
    def get_website_name():
        print(f"Enter website name:")
        website_name = input()
        return(website_name)

    # Asks for a password length from the user
    def get_password_length():
        print(f"Enter password length (minimum of 14):")
        password_length = input()
        PasswordGen.check_password_length(password_length)
        return(password_length)

    # Checks the password the user inputs for correct input type and correct length
    def check_password_length(password_length):
        if password_length.isnumeric() == False or int(password_length) < 14:
            password_length = PasswordGen.get_password_length()

    # Generates a password based on an input length
    def generate_password(password_length):
        password = ""
        for i in range(int(password_length)):
            chance = random.randint(0, 2)
            choice = ""
            if chance == 0:
                choice = random.choice(string.digits)
            elif chance == 1:
                choice = random.choice(string.ascii_letters)
            else:
                choice = random.choice(string.punctuation)

            password = f"{password}{choice}"

        return(password)
    
    # Decryptes a json file input

    # Encryptes a json file input