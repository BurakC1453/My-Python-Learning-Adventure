import sys
from tabulate import tabulate
import csv

def main():
    if len(sys.argv) != 2:
        print("You must provide pizza csv file as command-line argument")
        sys.exit(1)
    if not sys.argv[1].endswith(".csv"):
        print("File must be a csv")
        sys.exit(1)
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            print(tabulate(reader, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        print("File not found")
        sys.exit(1)
if __name__ == "__main__":
    main()