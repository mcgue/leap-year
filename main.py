# Calculate whether a year is a leap year

def explanation():
    # Print what the program is about
    print("I can determine if any year is a leap year")

def calculate(year):
    # Divide by 4
    if year % 4 == 0:
        return "This is a leap year"
    else:
        return "probably not"


if __name__ == '__main__':
    # Introduce program
    explanation()
    # Get input
    year = int(input("Enter the year would you like to check: "))
    print(calculate(year))
