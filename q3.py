def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    print(f"Case of current dictionary as {dct}")
    finaldct = dct
    finaldct[key] = value
    print(f"   Final dictionary as {finaldct}")
    return


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
update_dictionary({}, "name", "Alice")
update_dictionary({"age": 25}, "age", 26)
