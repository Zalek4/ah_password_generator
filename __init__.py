import utilities.utilities as AH_Util

def main():
    # Ask for a website this password is for
    website_name = AH_Util.PasswordGen.get_website_name()

    # Ask for the password length, and check to make sure it's a valid input
    password_length = AH_Util.PasswordGen.get_password_length()

    # Generate a password passed on the input we've been given
    password = AH_Util.PasswordGen.generate_password(password_length)

    print(f"Website : {website_name}")
    print(f"Password : {password}")

if __name__ == "__main__":
    main()

    print("Press any key to exit...")
    input()