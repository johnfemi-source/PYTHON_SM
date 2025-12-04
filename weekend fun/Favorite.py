# Create a locked box for the favorite number
favorite_number = 7

# Ask the user to guess
guess = int(input("Guess my favorite number: "))

# Check if the guess is correct
if guess == favorite_number:
    print("That's my favorite number!")
else:
    print("Nice try, guess again!")
