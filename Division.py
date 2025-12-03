# Get two integers from the user
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

# Perform safe division
if second_number != 0:
    result = first_number / second_number
    print(f"Result: {result}")
else:
    print("Cannot divide by zero")
