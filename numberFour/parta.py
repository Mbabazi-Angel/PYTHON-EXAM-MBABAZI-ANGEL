
def university(salary, yearsOfService):
    if yearsOfService > 4:
        bonus = 0.08
    elif yearsOfService == 3:
        bonus = 0.05
    else:
        bonus = 0

    netBonus = salary * bonus
    netSalary = salary + netBonus

    return netBonus, netSalary

def main():
    while True:
        try:
            salary = float(input("Enter your salary: "))
            yearsOfSservice = int(input("Enter employee's years of service: "))

            bonus, netSalary = university(salary, yearsOfSservice)

            print(f"Net bonus amount: {bonus}")
            print(f"Net salary amount: {netSalary}")

            choice = input("Do you want to continue: ")
            if choice != "yes":
                break
        except ValueError:
            print("Please enter correct values for salary and years of service.")

if __name__ == "__main__":
    main()
