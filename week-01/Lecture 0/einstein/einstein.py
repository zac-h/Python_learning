def main():
    mass = int(input("What is the mass in kg? "))
    print("E=", E(mass))

def E(m):
    return m * 300000000**2

main()
