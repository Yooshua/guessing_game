import random
# number_guesses = 0
play_again = "y"
high_score = 0

def start_game(high_score):
	random_number = random.randint(1,10)
	guessed_number = 0
	number_guesses = 0
	print("====================================\nWelcome to the Number Guessing Game!\n====================================\n")
	
	if high_score == 0:
		print("Welcome new player! Try your best to get the lowest number!\n")
	else:
		print(f"The current high score is {high_score} guesses. Try to do better!\n")
	while guessed_number != random_number:
		try:
			guessed_number = int(input("Guess a number between 1 and 10:  "))
			if guessed_number < 1 or guessed_number > 10:
				raise ValueError
			else:
				if guessed_number < random_number:
					print(f"{guessed_number} is too low!\n")
				elif guessed_number > random_number:
					print(f"{guessed_number} is too high!\n")
				number_guesses += 1
		except ValueError:
			print("That is not a proper intput. Please try again. Please only use numbers 1 through 10.\n")
	print(f"You guessed {guessed_number}, which is correct! Congratulations!\n")
	return number_guesses

while play_again != "n":
	number_guesses = start_game(high_score)
	
	# Check if high_score hasn't been set yet and set it for the first attempt.
	if high_score == 0:
		high_score = number_guesses
		if high_score == 1: # Grammar Check: if it's one use 'guess' else guesses
			print("You are aweseom! It only took you 1 guess. That's a new record!")
		else:
			print(f"You are aweseom! It only took you {high_score} guesses. That's a new record!")
			
	# If it has been set check to see if it's better than the current score.
	elif number_guesses < high_score:
		high_score = number_guesses
		if high_score == 1: # Grammar Check: if it's one use 'guess' else guesses
			print("You are aweseom! It only took you SINGLE guess. That's a new record!")
		else:
			print(f"You are aweseom! It only took you {high_score} guesses. That's a new record!")
	else:
		print(f"It took you {number_guesses} guesses. That's not a high score. Play again and try for the record!\n")
	play_again = input("\nWould you like to play again? [y]es/[n]o ")

print(f"\n\n===================\nYour high score was {high_score}!\nThanks for playing!\n===================")