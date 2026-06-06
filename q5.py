def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    print(f"Case of divisibility, numerator as {num} and divisor as {divisor}:")
    if not (isinstance(num, (int, float, complex)) and not isinstance(num, bool)):
        print(f"     {num} is not numeric")
        return False
    if not (isinstance(divisor, (int, float, complex)) and not isinstance(divisor, bool)):
        print(f"     {divior} is not numeric")
        return False
    quotient, remainder = divmod(num, divisor)
    print("  Quotient:", quotient)
    print("  Remainder:", remainder)
    if (remainder==0):
        print("  Divisibility True")
    else:
        print("  Divisibility False")
    return True


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
check_divisibility(10, 2)
check_divisibility(7, 3)
