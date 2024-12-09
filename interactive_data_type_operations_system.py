print("Choose a data type to perform operations on:")
print("1. Strings")
print("2. Numbers")
print("3. Booleans")
print("4. Additional Data Types (List, Tuple, Dictionary)")

choice = input("Enter the number of your choice (1-4): ")

if choice == '1':
    sentence = "Learning Python is fun!"
    print("Extracted substring: ", sentence[9:15])  # Extract "Python"
    print("Uppercase: ", sentence.upper())
    print("Modified sentence: ", sentence.replace("fun", "awesome"))

elif choice == '2':
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"Addition: {num1 + num2}")
    print(f"Subtraction: {num1 - num2}")
    print(f"Multiplication: {num1 * num2}")
    if num2 != 0:
        print(f"Division: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
    print(f"Power: {num1 ** num2}")

elif choice == '3':
    is_python_fun = True
    is_sunny = False
    print(f"AND operation: {is_python_fun and is_sunny}")
    print(f"OR operation: {is_python_fun or is_sunny}")
    print(f"NOT operation on is_python_fun: {not is_python_fun}")
    print(f"Comparison: 10 > 5 is {10 > 5}, 5 == 5 is {5 == 5}")

elif choice == '4':
    # List operations
    my_list = [1, "apple", True, 3.14]
    my_list.append("new element")
    print(f"Updated list: {my_list}")
    print(f"4th element in list: {my_list[3]}")

    # Tuple operations
    fruits = ("apple", "banana", "cherry")
    print(f"Tuple length: {len(fruits)}")
    try:
        fruits[1] = "orange"  # Tuples are immutable
    except TypeError:
        print("Error: Cannot modify a tuple.")

    # Dictionary operations
    my_dict = {"name": "Alice", "age": 30, "city": "New York"}
    print(f"Value for 'age': {my_dict['age']}")
    my_dict["country"] = "USA"
    print(f"Updated dictionary: {my_dict}")

else:
    print("Invalid selection. Please choose a valid option.")
