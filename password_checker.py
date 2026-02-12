# Simple Password Checker
#
# CS 3090 Block 2 Project
# Author: David Perry
# Version: 02/11/26
# 
# This script runs a simple password strength checker in the terminal.
# The user will be prompted to type a password, and the code will check the string for
# various strength markers and assign a score out of 6 points, with 6 being the highest
# possible score and meeting all requirements. If the password is missing one of the 
# requirements, it will tell the user to change something about the password to make it 
# stronger. 


# A list of some very common passwords to immediately flag if the user tries them
common_passwords = ["password", "123456", "qwerty", "abc123", "letmein", "admin", "123"]


# Function to check the characters in the input password
def analyze_characters(password):

    # Start all checkers as False
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False

    # Go through each character one at a time
    for char in password:

        # Check for lowercase letters
        if char.islower():
            has_lower = True

        # Check for uppercase letters
        elif char.isupper():
            has_upper = True

        # Check for numbers
        elif char.isdigit():
            has_digit = True

        # Anything else counts as a symbol
        elif not char.isalnum():
            has_symbol = True

    # Return all results of checkers together
    return has_lower, has_upper, has_digit, has_symbol


# Function that calculates the strength score
def check_strength(password):

    # Start score at 0
    score = 0

    # Keep track of suggestions to show the user
    feedback = []

    # Give a point if password is at least 8 characters
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Try making the password at least 8 characters long.")

    # Give another point if it is longer than 11 characters
    if len(password) >= 12:
        score += 1

    # Call helper function to analyze characters
    has_lower, has_upper, has_digit, has_symbol = analyze_characters(password)

    # Give points and suggestions based on results
    if has_lower:
        score += 1
    else:
        feedback.append("Add some lowercase letters.")

    if has_upper:
        score += 1
    else:
        feedback.append("Add some uppercase letters.")

    if has_digit:
        score += 1
    else:
        feedback.append("Add some numbers.")

    if has_symbol:
        score += 1
    else:
        feedback.append("Try adding a symbol like ! or @.")

    # If password matches a known common password, reset score
    if password.lower() in common_passwords:
        feedback.append("This looks like a very common password.")
        score = 0

    # Check if same character repeats 3 times in a row (like aaa or 111)
    for i in range(len(password) - 2):

        # Compare current char to next two chars
        if password[i] == password[i+1] == password[i+2]:
            feedback.append("Avoid repeating the same character many times.")
            score -= 1
            break

    # Make sure score never goes below 0
    if score < 0:
        score = 0

    # Return final results
    return score, feedback

# Header line
print("Simple Password Strength Checker\n")

# Ask user for a password
password = input("Enter a password to test: ")

# Call the checking function
score, feedback = check_strength(password)

# Print result section
print("\nPassword Strength Result:")

# Decide strength label based on score
if score <= 2:
    print("Weak password")
elif score <= 4:
    print("Moderate password")
else:
    print("Strong password")

# Show numeric score out of 6 possible points
print("Score:", score, "/ 6")

# Print suggestions
if feedback:
    print("\nSuggestions:")
    for tip in feedback:
        print("-", tip)

# Goodbye message
print("\nThank you for using the password strength checker!")