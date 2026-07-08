def main():
    sentence = input("What's your sentence? ")
    print(convert(sentence))


def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

main()
