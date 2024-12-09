print("Choose a data type to perform operations on:")  # Display the options to the user.
print("1. Strings")  # Option for string operations.
print("2. Numbers")  # Option for numerical operations.
print("3. Booleans")  # Option for boolean logic operations.
print("4. Additional Data Types (List, Tuple, Dictionary)")  # Option for other data types.

# Prompt the user to select one of the options.
choice = input("Enter the number of your choice (1-4): ")

# If the user selects option 1 (Strings):
if choice == '1':
    sentence = "Learning Python is fun!"  # Define a sample sentence for operations.
    print("Extracted substring: ", sentence[9:15])  # Extract the substring "Python" (characters at indices 9 to 14).
    print("Uppercase: ", sentence.upper())  # Convert the entire string to uppercase.
    print("Modified sentence: ", sentence.replace("fun", "awesome"))  # Replace "fun" with "awesome".

# If the user selects option 2 (Numbers):
elif choice == '2':
    num1 = float(input("Enter the first number: "))  # Prompt the user to input the first number and convert it to a float.
    num2 = float(input("Enter the second number: "))  # Prompt the user to input the second number and convert it to a float.
    print(f"Addition: {num1 + num2}")  # Perform addition and print the result.
    print(f"Subtraction: {num1 - num2}")  # Perform subtraction and print the result.
    print(f"Multiplication: {num1 * num2}")  # Perform multiplication and print the result.
    if num2 != 0:  # Check if the second number is not zero to avoid division by zero.
        print(f"Division: {num1 / num2}")  # Perform division and print the result.
    else:
        print("Error: Division by zero is not allowed.")  # Print an error message for division by zero.
    print(f"Power: {num1 ** num2}")  # Calculate the power (num1 raised to num2) and print the result.

# If the user selects option 3 (Booleans):
elif choice == '3':
    is_python_fun = True  # Define a boolean variable with the value True.
    is_sunny = False  # Define another boolean variable with the value False.
    print(f"AND operation: {is_python_fun and is_sunny}")  # Perform a logical AND operation and print the result.
    print(f"OR operation: {is_python_fun or is_sunny}")  # Perform a logical OR operation and print the result.
    print(f"NOT operation on is_python_fun: {not is_python_fun}")  # Perform a NOT operation and print the result.
    print(f"Comparison: 10 > 5 is {10 > 5}, 5 == 5 is {5 == 5}")  # Perform and print the results of comparison operations.

# If the user selects option 4 (Additional Data Types):
elif choice == '4':
    # List operations
    my_list = [1, "apple", True, 3.14]  # Define a sample list with mixed data types.
    my_list.append("new element")  # Add a new element to the end of the list.
    print(f"Updated list: {my_list}")  # Print the updated list.
    print(f"4th element in list: {my_list[3]}")  # Access and print the 4th element in the list (index 3).

    # Tuple operations
    fruits = ("apple", "banana", "cherry")  # Define a tuple with three elements.
    print(f"Tuple length: {len(fruits)}")  # Print the length of the tuple.
    try:
        fruits[1] = "orange"  # Attempt to modify the second element of the tuple.
    except TypeError:  # Catch the error because tuples are immutable.
        print("Error: Cannot modify a tuple.")  # Print an error message.

    # Dictionary operations
    my_dict = {"name": "Alice", "age": 30, "city": "New York"}  # Define a dictionary with key-value pairs.
    print(f"Value for 'age': {my_dict['age']}")  # Access and print the value associated with the key 'age'.
    my_dict["country"] = "USA"  # Add a new key-value pair to the dictionary.
    print(f"Updated dictionary: {my_dict}")  # Print the updated dictionary.

# If the user enters an invalid option:
else:
    print("Invalid selection. Please choose a valid option.")  # Notify the user of an invalid choice.
