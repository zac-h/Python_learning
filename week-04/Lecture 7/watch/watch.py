import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    url = re.search(r'^<iframe[^>].*src="https?://(?:www\.)?youtube\.com/embed/([^"]*)"[^>]*', s, re.IGNORECASE)
    if not url:
        return None

    return "https://youtu.be/" + url.group(1).rsplit("/",1)[-1]


if __name__ == "__main__":
    main()
