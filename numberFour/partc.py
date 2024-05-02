import math

def maps(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1)*2 + (y2 - y1)*2)
    return d

def main():
    while True:
        try:
            x1 = float(input("Enter X1: "))
            y1 = float(input("Enter Y1: "))
            x2 = float(input("Enter X2: "))
            y2 = float(input("Enter Y2: "))

            d = maps(x1, y1, x2, y2)

            print(f"The distance between the two points is: {d} units")

            choice = input("Do you want to continue: ")
            if choice != "yes":
                break
        except ValueError:
            print("Please enter right values.")

if __name__ == "__main__":
    main()
