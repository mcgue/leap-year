# Calculate whether a year is a leap year

def explanation():
    # Print what the program is about
    print("I can determine if any year is a leap year")

def calculate(year):
    # Divide by 4
    if year >= 1582:
        if year % 400 == 0:
            if year % 4 == 0:
                return "This is a leap year with an extra day on February 29th"
        elif (year % 400 != 0) or (year % 4 != 0):
            return "This is not a leap year"
        else:
            return "huh?"
    elif year > -46:
        return "This was a year during the Julian Calendar.\n" \
               "At the time, leap day was February 24.\n" \
               "February was the last month of the year."



if __name__ == '__main__':
    # Introduce program
    explanation()
    # Get input
    year = int(input("Enter the year would you like to check: "))
    print(calculate(year))
