def roman_to_int(s: str) -> int:
    # Your conversion function
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for numeral in reversed(s):
        value = roman_map.get(numeral, 0)  # Default to 0 for invalid characters
        total, prev_value = (total - value, value) if value < prev_value else (total + value, value)
    return total

# Loop until user decides to quit
while True:
    user_input = input("Enter a Roman numeral (or press 'q' to quit): ")
    if user_input.lower() == 'q':  # Check if the user wants to quit
        break  # Exit the loop

    # Convert and display the result
    try:
        result = roman_to_int(user_input.upper())  # Convert input to uppercase to match the keys in the map
        print(f"The integer value of {user_input} is {result}")
    except Exception as e:
        print(f"An error occurred: {e}")

print("Program ended.")
