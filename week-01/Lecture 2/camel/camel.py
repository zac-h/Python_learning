name = input("What's the variable name in camel case?: ").strip()

for _ in range(len(name)):
    if name[_].islower():
        print(name[_], end="")
    else:
        print("_" + name[_].lower(), end="")


print("")
