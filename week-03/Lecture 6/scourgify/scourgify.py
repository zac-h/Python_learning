import sys
import csv

try:
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        raise ValueError
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        raise ValueError
    elif not sys.argv[1].lstrip().endswith(".csv"):
        print("Not a .csv file")
        raise ValueError
    else:
        try:
            before_list = []
            after_list = []
            with open(sys.argv[1], "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    before_list.append({"name": row["name"], "house": row["house"]})
                for student in before_list:
                    name = student["name"]
                    house = student["house"]
                    last_name, first_name = [part.strip() for part in name.split(",")]
                    after_list.append({"first_name": first_name, "last_name": last_name, "house": house})
            with open(sys.argv[2], "w") as file:
                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in after_list:
                    writer.writerow({"first": row["first_name"], "last": row["last_name"], "house": row["house"]})
        except FileNotFoundError:
            print("File does not exist")
            sys.exit(1)
except ValueError:
    sys.exit(1)
