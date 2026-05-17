def safe_divide():
    try:
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")

    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")

    except ValueError:
        print("Error: Please enter valid numbers.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")



while True:
    safe_divide()
