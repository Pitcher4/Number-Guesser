import random

# Choosing a pseudorandom number using the random library
number = random.randint(1, 100)
# Defining the constant number of guesses
NUMBER_OF_GUESSES = 10

won = False

# Iterating the number of guesses using a for loop
for i in range(NUMBER_OF_GUESSES):
	# Ask the user to guess
	guess = int(input("What is your guess? Pick between 1 and 100: "))

	# Check for win
	if number == guess:
		print("Correct!")
		won = True
		break
	# Check if number too high
	elif guess > number:
		print("Your guess was too high")
	# Check if number too low
	elif guess < number:
		print("Your guess was too low.")

# Ternary operator to print message if the player does not win
print(f"You have run out of guesses! The answer was {number}." if not won else "")