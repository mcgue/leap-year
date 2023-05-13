# Calculate whether a year is a leap year

# Function to calculate whether a leap year
def calculate(year):
    # Leap years not invented yet
    if year < -45:
        return "Leap years had not started yet. Caesar implemented \n" \
               "them in 45 bce."
    # Divide by 4
    elif year % 4 != 0:
        return "This is not a leap year"
    elif year >= 1582:
        if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            return "For those places using the Gregorian \n" \
                    "calendar, this is/was a leap year with \n" \
                    "an extra day on February 29th"
        else:
            return "This is not a leap year"
    else:
        return "This was a leap year during the Julian Calendar.\n" \
               "At the time, leap day was an extra February 24th\n" \
               "and February was the last month of the year."

if __name__ == '__main__':
    # Introduce program
    print("I can determine if any year is a leap year")
    # Get input
    year = int(input("Enter the year would you like to check: "))
    # Run program to determine whether year is a leap year
    print(calculate(year))
