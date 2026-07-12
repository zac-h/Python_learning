def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            print("Input must be integer/integer and denominator cannot be zero.")
            pass

def convert(fraction):
        x , y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x>y or x<0 or y<0:
            raise ValueError
        return round((x/y)*100)


def gauge(percentage):
    if percentage <= 1:
        return f"E"
    elif percentage >= 99:
        return f"F"
    else:
        return f"{percentage}%"
#    break

if __name__ == "__main__":
    main()




