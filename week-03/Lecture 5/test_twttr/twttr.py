def main():
    word = input("What's the word? ").strip()
    print(shorten(word))

def shorten(word):
    result = ""
    for _ in range(len(word)):
        if word[_] not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            result += word[_]
    return result

if __name__ == "__main__":
    main()
