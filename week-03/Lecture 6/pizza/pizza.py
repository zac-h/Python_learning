import sys
import csv
from tabulate import tabulate

try:
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        raise ValueError
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        raise ValueError
    elif not sys.argv[1].lstrip().endswith(".csv"):
        print("Not a .csv file")
        raise ValueError
    else:
        try:
            with open(sys.argv[1], "r") as file:
                reader = csv.reader(file)
                print(tabulate(reader, headers="firstrow", tablefmt="grid"))
        except FileNotFoundError:
            print("File does not exist")
            sys.exit(1)
except ValueError:
    sys.exit(1)
