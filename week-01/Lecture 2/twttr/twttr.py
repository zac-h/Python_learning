word = input("What's the word? ").strip()


for _ in range(len(word)):
    if word[_] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        print(end="")
    else:
        print(word[_], end="")
print()
