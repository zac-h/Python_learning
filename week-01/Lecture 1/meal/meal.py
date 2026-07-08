def main():
    time = input("What's the time? ")
    time = convert(time)

    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")
    else:
        print("")

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return (hours + minutes/60)


if __name__ == "__main__":
    main()
