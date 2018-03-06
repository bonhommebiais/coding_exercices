import random

# This is a short game which helps you guess a number between 0 and 50.

chosen_nbr = random.randint(0,50)
number = input("Guess my chosen number between 0 and 50: ")
while chosen_nbr != number:
	if chosen_nbr > number:
		number = input("Guess a higher number: ")
	else:
		number = input("Guess a smaller number: ")
print "You guessed it!"




