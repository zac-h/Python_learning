

cost = 50

while True:
    coin = int(input("What's the coin? "))
    if coin not in [5, 10, 25]:
        print(f"Amount due: {cost}")
        continue
    cost = cost - coin
    if cost >0:
        print(f"Amount due: {cost}")
    elif cost <= 0:
        print("Change owed: " + str(cost*-1))
        break

