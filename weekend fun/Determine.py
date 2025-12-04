# Get age from the user
age = int(input("Enter your age: "))

# Determine ticket price based on age
if age < 5:
    print("Free")
elif age >= 5 and age <= 12:
    print("$5")
elif age >= 13 and age <= 64:
    print("$12")
else:  # 65 or older
    print("$8")
