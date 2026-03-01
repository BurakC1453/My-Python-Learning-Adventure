import sys
import inflect
from datetime import date 

def main():
    date_of_birth = input("Please enter your date of birth (YYYY-MM-DD).")
    try:
        date_of_birth = date.fromisoformat(date_of_birth)
    except ValueError:
        print("Please provide the date in ISO format (YYYY-MM-DD).")
        sys.exit("Invalid date format.")
    todays_date = date.today()
    difference = todays_date - date_of_birth
    difference = difference.days
    difference = difference*1440
    difference_in_words = inflect.engine().number_to_words(difference)
    print(f"{difference_in_words} minutes")

if __name__ == "__main__":
    main()