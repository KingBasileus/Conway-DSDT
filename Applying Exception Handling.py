while True:
    try:
        num1 = float(input("Please enter a number "))
        num2 = float(input("Please enter a number "))

        result = num1 + num2
        print("Addded together they equal: ", result)
        break

    except ValueError:
        print("Oops! That was not a valid number. Please try again.")