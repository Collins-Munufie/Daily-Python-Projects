def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x / y

def divide(x,y):
    if y == 0:
        raise ValueError("Cannot divide by Zero")
    return x / y

def modulus(x, y):
    if y == 0:
        raise ValueError ("Cannot divide by Zero")
    return x % y

def power(x, y):
    return x ** y

print ("Welcome to the Simple Calculator. Have fun 🤣🤣🤣 and Enjoy it")
print ("Select operation you want to perform")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print ("4. Division")
print ("5. Modulus")
print ("6. Power")

choice = input("Enter your choice (1/2/3/4):")


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number:"))

    if choice =='1':
        print (f"Result:{num1} +{num2} = {add(num1, num2)}")

    elif choice == '2':
        print (f"Result:{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print (f"Result:{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print (f"Result:{num1} / {num2} = {divide(num1, num2)}")

    else: 
      ("Invalid input Please Enter a valid choice from 1, 2, 3 or 4")
except ValueError as e:
    print(f"Error: {e}. Please enter valid numbers.")
                