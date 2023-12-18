import utilities.pg_logging as pg_logging
import utilities.pg_password as pg_password
log = pg_logging.PG_Logging.pg_log

def main():
    # Ask for a website this password is for
    website_name = pg_password.PG_Password.pg_get_website_name()

    # Ask for the password length, and check to make sure it's a valid input
    password_length = pg_password.PG_Password.pg_get_password_length()

    # Generate a password passed on the input we've been given
    password = pg_password.PG_Password.pg_generate_password(password_length)

    # Decrypt our json file if it exists, and create it if it doesn't

    # Write our new website/password combination to a json file

    # Encrypt the new json file

    print(f"Website : {website_name}")
    print(f"Password : {password}")

if __name__ == "__main__":
    log(1, f"__name__ == '__main__'")
    main()

    log(1, f"Press any key to exit...")
    input()