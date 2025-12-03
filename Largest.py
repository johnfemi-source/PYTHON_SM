# Get three integers from the user
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Find the largest number using only two if statements
largest = number1

if number2 > largest:
    largest = number2

if number3 > largest:
    largest = number3

print(f"The largest number is: {largest}")
