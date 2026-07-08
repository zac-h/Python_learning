import emoji

text = input("Input: ")
message = emoji.emojize(text, language='alias')
print(message)
