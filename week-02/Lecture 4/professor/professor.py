import random


def main():
    x=[]
    y=[]

    level = get_level()

    for _ in range(10):
        x.append(generate_integer(level))
        y.append(generate_integer(level))

    correct = 0
    
    for _ in range(10):
        incorrect = 0
        while True:
            answer = int(input(f"{x[_]} + {y[_]} = "))
            if answer == x[_] + y[_]:
                correct += 1
                break
            else:
                incorrect += 1
                print("EEE")
                if incorrect == 3:
                    print(f"{x[_]} + {y[_]} = {x[_]+y[_]}")
                    break
    print(f"Score: {correct}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n not in [1, 2, 3]:
                raise ValueError
            return n
        except ValueError:
            pass


def generate_integer(level):
    while True:
        try:
            if level == 1:
                integer = random.randint(0, 9)
                return integer
            elif level ==2:
                integer = random.randint(10, 99)
                return integer
            elif level == 3:
                integer = random.randint(100,999)
                return integer
            else:
                raise ValueError
        except ValueError:
            break


if __name__ == "__main__":
    main()
