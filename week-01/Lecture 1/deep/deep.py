
answer = input("What's the answer to the great question? ").strip().lower()

match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
