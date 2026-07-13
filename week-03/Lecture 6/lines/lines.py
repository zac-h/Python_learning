import sys

try:
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        raise ValueError
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        raise ValueError
    elif not sys.argv[1].lstrip().endswith(".py"):
        print("Not a python file")
        raise ValueError
    else:
        try:
            count = 0
            with open(sys.argv[1], "r") as file:
                lines = file.readlines()
            for line in lines:
                if not line.lstrip().startswith("#") and line.strip() != "":
                    count += 1
            print(count)
        except FileNotFoundError:
            print("File does not exist")
except ValueError:
    sys.exit(1)
