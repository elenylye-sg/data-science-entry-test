def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    print(f"Case of list as {lst}")
    print(f"  Replacing {find_val} with {replace_val}")
    finallst = lst
    for index, value in enumerate(finallst):
        if value == find_val:
            finallst[index] = replace_val
    print(f"  Final list is {lst}")
    return


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"
find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
find_and_replace(["apple", "banana", "apple"], "apple", "orange")

# Result as follows:
'''
Case of list as [1, 2, 3, 4, 2, 2]
  Replacing 2 with 5
  Final list is [1, 5, 3, 4, 5, 5]
Case of list as ['apple', 'banana', 'apple']
  Replacing apple with orange
  Final list is ['orange', 'banana', 'orange']
'''
