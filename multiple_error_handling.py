while True:
    try:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        if not num1.strip() or not num2.strip():
            raise ValueError("Input cannot be empty.")

        num1 = float(num1)
        num2 = float(num2)

        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is {result}")
        break  

    except ValueError as ve:
        print(f"ValueError: {ve} Please enter valid numeric input.")

    except ZeroDivisionError:
        print("ZeroDivisionError: You cannot divide by zero. Try again.")

    except TypeError:
        print("TypeError: Invalid operation on provided input types.")

    except Exception as e:
        print(f"Unexpected error: {e}. Please try again.")
