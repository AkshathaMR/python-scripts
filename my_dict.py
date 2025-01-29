# Define a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Input value to check
value_to_check = input("Enter the value to check: ")

# Check if the value exists in the dictionary
if value_to_check in my_dict.values():
    print(f"The value '{value_to_check}' is found in the dictionary.")
else:
    print(f"The value '{value_to_check}' is not found in the dictionary.")

