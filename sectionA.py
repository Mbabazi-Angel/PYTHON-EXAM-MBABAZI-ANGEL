#(a)(i)
def studentGrades(mark):
    
    if  mark >=90 <=100:
        print('Grade is A')
    elif mark >=80 <=89:
        print('Grade is B')
    elif mark >=70 <=79:
        print('Grade is C')
    elif mark >=60 <=69:
        print('Grade is D')
    elif mark >=50 <=59:
        print('Grade is E')
    else:
        print('Fail')

studentGrades(int(input("Enter your mark:")))        
            


#(ii)
def celsius_to_fahrenheit(C):
    fahrenheit = (9/5) * C + 32
    return fahrenheit

def fahrenheit_to_celsius(F):
    celsius = (F - 32) * 5/9
    return celsius

def main():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter your choice 1,2: ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    else:
        print("Choose 1 or 2")

if __name__ == "__main__":
    main()
  



#(b)(i)
def areaOfTriangle(b,h):
    A = 1/2 * b * h

    print (f'The area of a triangle is {A}')

areaOfTriangle(2,3)


#(ii)
#sample list = [9,2,3,5,8]
def sumOfNumbers(list):
    total = 0
    for num in list:
        total += num
    return total

numbers_list = [9, 2, 3, 5, 8]
output = sumOfNumbers(numbers_list)
print("Sum of the numbers in the list:", output)
