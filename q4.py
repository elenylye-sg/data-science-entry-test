def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    print(f"Case of string as \"{s}\":")
    if isinstance(s, str):
        reversed_data = s[::-1]
        print("  ", reversed_data)
    else:
        print("  The variable is not a string.")
    return


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
string_reverse("Hello World")
string_reverse("Python")
