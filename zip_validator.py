import os
from zip_validator import validate


def display_title_bar():
    print("**********************************************")
    print("***  Zip Code Validator  ***")
    print("Validates a Zip Code using the following rules:")
    print("1 - The number must be greater than 100000")
    print("2 - The number must be less than 999999")
    print("3 - The number can't has a duplicate alternate digit in pairs.")

    print("\nExamples:")
    print("\t1. 100 - Invalid - Not greater than 100000")
    print("\t2. 100000 - Invalid - Not greater than 100000")
    print("\t3. 123456 - Valid")
    print("\t4. 121426 - Invalid - Digit 1 is duplicated alternated in pair")
    print("\t5. 523563 - Valid - Between maximum and minimum, and no alternate duplicated in pairs")
    print("\t5. 552523 - Invalid - Digit 2 is duplicated alternated in pair")

    print("**********************************************")


def get_user_choice():
    # Let users know what they can do.
    print("What number you would like to validate? ")
    print("Press [q] to quit.")

    return input("")


display_title_bar()

input_value = ''
while input_value != 'q':
    input_value = get_user_choice()

    if input_value != 'q':
        if validate(input_value):
            print(input_value + " is a valid number!")
        else:
            print(input_value + " is not a valid number. ")

    print("\n")
