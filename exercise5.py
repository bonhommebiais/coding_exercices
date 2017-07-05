print "Disclaimer: You must always enter a letter otherwie the program will end. Press space then enter if you desire to end the game."


word = raw_input("Enter a word: ")
searched_letter = raw_input("Enter a letter: ")
while searched_letter != " ":
	count = 0
	if searched_letter in word:
		for letter in word:
			if searched_letter == letter:
				count = count + 1
		print searched_letter + " is in the word " + word + " " + str(count) + " times." 
	else:
		print searched_letter + " is not in the word " + word
	searched_letter = raw_input("Enter a letter: ")

