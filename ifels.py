def method1():
    # Positive, Negative, or Zero
    num = int(input("Enter a number: "))
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")

def method2():
    # Even, Odd, or Not an Integer
    num = input("Enter something: ")
    if num.isdigit():
        num = int(num)
        if num % 2 == 0:
            print("Even number")
        else:
            print("Odd number")
    else:
        print("Not an integer")

def method3():
    # Grade System
    marks = int(input("Enter marks: "))
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 50:
        print("Grade C")
    else:
        print("Fail")

def method4():
    # Age Category
    age = int(input("Enter your age: "))
    if age < 13:
        print("Child")
    elif age < 20:
        print("Teenager")
    elif age < 60:
        print("Adult")
    else:
        print("Senior Citizen")

def method5():
    # Simple Calculator
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")
    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        print("Result:", a / b)
    else:
        print("Invalid operator")

# Main Menu
while True:
    print("\n--- If-Elif-Else 5 Methods Menu ---")
    print("1. Positive/Negative/Zero")
    print("2. Even/Odd/Not Integer")
    print("3. Grade System")
    print("4. Age Category")
    print("5. Calculator")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        method1()
    elif choice == "2":
        method2()
    elif choice == "3":
        method3()
    elif choice == "4":
        method4()
    elif choice == "5":
        method5()
    elif choice == "6":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice, try again!")
