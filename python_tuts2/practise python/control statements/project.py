
    
num_1 =float(input("Enter first number: "))
num_2 =float(input("Enter second number: "))
operator = input("Enter operator: ")
#choice=input("enter your choice + - * - ")
# if choice == "+":
#     print(num_1 + num_2)
# elif choice == "-":
#     print(num_1 - num_2)
# elif choice == "*":
#     print(num_1 * num_2)
# elif choice == "/":
#     print(num_1 / num_2)
# elif choice == "%":
#     print(num_1 % num_2)
# elif choice == "^":
#     print(num_1 ** num_2)
# else:
#     print("Invalid operator")


match (operator):
    case "+":
      print(num_1 + num_2)
    case "-":
        print(num_1 - num_2)
    case "*":
        print(num_1 * num_2)
    case "/":
        print(num_1 / num_2)
    case "%":
        print(num_1 % num_2)
    case "^":
        print(num_1 ** num_2)
    case _:
        print("Invalid operator")