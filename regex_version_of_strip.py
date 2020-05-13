# regex_version_of_strip
# Write function that takes a string and does the same thing as the strip() string method
import re

# Method to take string as input & then whitespace characters will be removed from the beginning and end of the string
def strip(text):
    # To remove the spaces if present at starting of the word.^ indicates the starting of string
    textStartRegex = re.compile(r'(^\s*)')

    # To remove the spaces if present at the end of the word.$ indicates the ending of the string
    textEndRegex = re.compile(r'(\s*$)')

    startStrip = textStartRegex.sub('', text)
    endStrip = textEndRegex.sub('', startStrip)
    return endStrip


# main method
if __name__ == "__main__":
    # Take input from user
    inputData = input("Give some text:")
    print("After using strip Function:" + strip(inputData))
