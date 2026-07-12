def main():
    greeting = input("What's the greeting? ").strip().lower()
    print(f"${value(greeting)}")


def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting[:1] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()





