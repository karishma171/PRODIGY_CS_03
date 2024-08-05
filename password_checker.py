import re

def check_password_complexity(password):
    # Check the length of the password
    length_criteria = len(password) >= 8

    # Check for uppercase letters
    uppercase_criteria = re.search(r'[A-Z]', password) is not None

    # Check for lowercase letters
    lowercase_criteria = re.search(r'[a-z]', password) is not None

    # Check for digits
    digit_criteria = re.search(r'\d', password) is not None

    # Check for special characters
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Assess the strength of the password
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])
    
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Medium"
    else:
        strength = "Weak"

    # Provide feedback
    feedback = "Password Strength: " + strength + "\n"
    feedback += "Criteria Met: " + str(criteria_met) + "/5\n"
    feedback += "Length (>= 8): " + str(length_criteria) + "\n"
    feedback += "Uppercase Letters: " + str(uppercase_criteria) + "\n"
    feedback += "Lowercase Letters: " + str(lowercase_criteria) + "\n"
    feedback += "Digits: " + str(digit_criteria) + "\n"
    feedback += "Special Characters: " + str(special_char_criteria) + "\n"

    return feedback

def main():
    # Get the password from the user
    password = input("Enter a password to check its strength: ")
    # Check the password complexity
    result = check_password_complexity(password)
    # Print the result
    print(result)

if __name__ == "__main__":
    main()
