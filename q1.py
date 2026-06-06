

def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    print(f"Case of swapping x as {x} and y as {y}:")
    if not (isinstance(x, (int, float, complex)) and not isinstance(x, bool)):
        print('     x is not numeric')
        return -1
    if not (isinstance(y, (int, float, complex)) and not isinstance(y, bool)):
        print('     y is not numeric')
        return -1
    tmp = x 
    x = y   
    y = tmp
    print(f"     After swap, x is {x} and y is {y}")
    return 0

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
swap("Apple", 10)
swap(9, 17)

