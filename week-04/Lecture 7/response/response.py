import sys
from validator_collection import validators, errors


def main():
    print(validate(input("Email: ")))


def validate(s):
    try:
        validators.email(s, allow_empty = False)
        return f"Valid"
    except errors.InvalidEmailError:
        return f"Invalid"
    except errors.EmptyValueError:
        return f"Invalid"


if __name__ == "__main__":
    main()
