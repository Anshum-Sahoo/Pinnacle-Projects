while True:
    try:
        Num_1 = float(input("Enter first number: "))
        Num_2 = float(input("Enter second number: "))
        Op = input("Enter operator (+,-,*,/,//,%) or q to quit: ")

        if Op.lower() == "q":
            break

        match Op:
            case "+":
                print("Sum:", Num_1 + Num_2)
            case "-":
                print("Difference:", Num_1 - Num_2)
            case "*":
                print("Product:", Num_1 * Num_2)
            case "/":
                print("Division:", Num_1 / Num_2)
            case "//":
                print("Floor Division:", Num_1 // Num_2)
            case "%":
                print("Remainder:", Num_1 % Num_2)
            case _:
                print("Invalid operator!")

    except ValueError:
        print("Please enter valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")

