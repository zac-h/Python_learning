import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    um_list = re.findall(r"\bum\w*", s)
    return um_list.count("um")

if __name__ == "__main__":
    main()
