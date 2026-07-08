import random

while True:
    try:
        n = int(input("Level: "))
        if n<= 0:
            raise ValueError
        number = random.randint(1, n)
        break
    except ValueError:
        pass

while True:
    try:
        guess = int(input("Guess: "))
        if guess <=0:
            raise ValueError
        elif 0 < guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass



