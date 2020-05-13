# strong_password_detection.py
# Use regular expressions to make sure the password string which is passed is strong or not

# importing the modeule re to use regex functions
import re


# Method to check strength of given password
def checkPasswordStrength(password):
    # compile method return regex pattern object & r is used to consider the given string as raw string
    # for password to have at least 8 characters
    eightCharLongRegex = re.compile(r'[\d\w\s\D\W\S]{8,}')

    # for password to have uppercase characters
    upperCaseRegex = re.compile(r'[A-Z]+')

    # for password to have lowercase characters
    lowerCaseRegex = re.compile(r'[a-z]+')

    # for password to have at least one digit
    forOneOrMoreDigitRegex = re.compile(r'\d+')

    if not eightCharLongRegex.search(password):
        return "Your password should have at least eight characters,both uppercase and lowercase characters and at least one digit"

    elif not upperCaseRegex.search(password):
        return "Your password should have at least eight characters,both uppercase and lowercase characters and at least one digit"

    elif not lowerCaseRegex.search(password):
        return "Your password should have at least eight characters,both uppercase and lowercase characters and at least one digit"

    elif not forOneOrMoreDigitRegex.search(password):
        return "Your password should have at least eight characters,both uppercase and lowercase characters and at least one digit"

    return "Your password is Strong!"


# main method
if __name__ == "__main__":
    # input is used to take password from user
    password = input("Please enter your password:")
    print(checkPasswordStrength(password))
