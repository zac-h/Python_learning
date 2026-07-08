greeting = input("What's the greeting? ").strip().lower()

if greeting.startswith("hello"):
    print("$0")
elif greeting[:1] == "h":
    print("$20")
else:
    print("$100")
