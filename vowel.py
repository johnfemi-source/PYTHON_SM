
# Program to count vowels and consonants in a string

string = input("Enter a word or sentence: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in string:
    if char.isalpha():  # Check if it's a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)

