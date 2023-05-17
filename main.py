# Calculate whether a year is a leap year

from datetime import datetime

# Function to calculate whether a leap year
def calculate(year):
    # Determine current year
    today = datetime.now().year
    # if current year
    if year == today:
        verb = 'is'
        verb_neg = verb
    # If in the future
    elif year > today:
        verb = 'will be'
        verb_neg = 'will not be'
    # If the past
    else:
        verb = 'was'
        verb_neg = verb
    # If before leap year invention
    if year < -45:
        return "Leap years had not yet started. Caesar implemented \n" \
               "them in 45 BCE."
    # If not divisible by 4
    elif year % 4 != 0:
        return f"This {verb_neg} a leap year"
    # If after implementation of Gregorian calendar
    elif year >= 1582:
        # Yes to leap year if divisible by 4 and only years divisible by 400
        if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            return "For those places using the Gregorian \n" \
                    f"calendar, this {verb} a leap year with \n" \
                    "an extra day on February 29th"
        else:
            return f"This {verb_neg} a leap year"
    # Remaining are leap years in Julian Calendar
    else:
        return "This was a leap year during the Julian Calendar.\n" \
               "At the time, leap day was an extra February 24th\n" \
               "and February was the last month of the year."

if __name__ == '__main__':
    # Introduce program
    print("I can determine if any year is a leap year. Enter a negative if BCE")
    # Get input
    year = int(input("Enter the year would you like to check: "))
    # Run function to determine whether year is a leap year
    print(calculate(year))
