# Simple Calculator (beginner version)

while True:
    print("\n===== Simple Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Module (remainder)")
    print("6. Exit")

    operation = input("Select operation (1-6): ")

    # Exit the program
    if operation == "6":
        print("Goodbye!")
        break

    # Only ask for numbers if the choice is 1 to 5
    if operation == "1" or operation == "2" or operation == "3" or operation == "4" or operation == "5":
        num_1 = int(input("Enter the first number: "))
        num_2 = int(input("Enter the second number: "))

        if operation == "1":
            result = num_1 + num_2
            print(f"Addition result: {result}")

        elif operation == "2":
            result = num_1 - num_2
            print(f"Subtraction result: {result}")

        elif operation == "3":
            result = num_1 * num_2
            print(f"Multiplication result: {result}")

        elif operation == "4":
            if num_2 == 0:
                print("Error: You cannot divide by zero.")
            else:
                result = num_1 / num_2
                print(f"Division result: {result}")

        elif operation == "5":
            if num_2 == 0:
                print("Error: You cannot get a remainder when dividing by zero.")
            else:
                result = num_1 % num_2
                print(f"Module result: {result}")

    else:
        print("Invalid selection. Please choose a number from 1 to 6.")