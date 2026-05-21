try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    try:
        result = num1 / num2
        print("Result: ", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except Exception as e:
    print("An error occurred: ", str(e))