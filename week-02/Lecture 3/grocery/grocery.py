

list = {}

while True:
    try:
        item = input("").upper()
        if item in list:
            list[item] += 1
        else:
            list[item] = 1
    except KeyError:
        continue
    except EOFError:
        print("")
        for item in sorted(list):
            print(list[item], item, sep=" ")
        break

