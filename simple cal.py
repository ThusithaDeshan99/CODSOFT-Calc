while True:
    print("Select operation:")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    operation = input("Enter your choice : ")

    if operation == "5":
        print("Exiting. Goodbye!")
        break  

    if operation in ("1", "2", "3", "4"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == "1":
            result = num1 + num2
            print(f"The answer is: {num1} + {num2} = {result}")

        elif operation == "2":
            result = num1 - num2
            print(f"The answer is: {num1} - {num2} = {result}")

        elif operation == "3":
            result = num1 * num2
            print(f"The answer is: {num1} * {num2} = {result}")

        elif operation == "4":
            if num2 != 0:
                result = num1 / num2
                print(f"The answer is: {num1} / {num2} = {result}")
            else:
                print("Cannot divide by zero")

    else:
        print("Invalid input")

    another_operation = input("Do you want to go trough another operation? (yes/no): ")
    if another_operation.lower() != "yes":
        print("Exiting. Goodbye!")
        break 
