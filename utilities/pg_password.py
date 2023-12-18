import random
import string

class PG_Password():
    # Asks for a website name from the user
    def pg_get_website_name():
        print(f"Enter website name:")
        website_name = input()
        return(website_name)

    # Asks for a password length from the user
    def pg_get_password_length():
        print(f"Enter password length (minimum of 14):")
        password_length = input()
        PG_Password.pg_check_password_length(password_length)
        return(password_length)

    # Checks the password the user inputs for correct input type and correct length
    def pg_check_password_length(password_length):
        if password_length.isnumeric() == False or int(password_length) < 14:
            password_length = PG_Password.pg_get_password_length()

    # Generates a password based on an input length
    def pg_generate_password(password_length):
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
    
    # Writes a website/password combination to a json file
    
    # Decryptes a json file input

    # Encryptes a json file input