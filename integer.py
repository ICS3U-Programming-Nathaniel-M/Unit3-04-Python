#!/usr/bin/env python3
# Created By: Nathaniel
# Date: October 2, 2025
# Write what this program does.


def main():
    # Get number
    user_input = int(input("Enter a positive, negative or zero integer: "))
    # Check if the number is negative
    if user_input < 0:
        print("This is a negative number.")
    # Otherwise, check if the number is positive
    elif user_input > 0:
        print("This is a positive number.")
    # Otherwise, must be zero
    else:
        print("This is zero.")


if __name__ == "__main__":
    main()
