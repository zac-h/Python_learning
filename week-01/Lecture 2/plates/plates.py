import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (s[:2].isalpha()
        and 2<= len(s) <=6
        and no_middle_num(s)
        and no_punctuation(s)
        and first_number_is_not_zero(s)
    ):
        return True


def no_middle_num(s):
    found_number = False
    for character in s:
        if character.isdigit():
            found_number = True
        elif found_number == True:
            return False
    return True

def no_punctuation(text):
    if any(char in string.punctuation for char in text): #returns true if the is any punctuation present
        return False #so return false i.e failed the no punctuation check
    else:
        return True

def first_number_is_not_zero(text):
    for character in text:
        if character.isdigit():
            return character != "0"
    return True



main()
