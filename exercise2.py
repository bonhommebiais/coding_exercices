word = raw_input("Enter a word: ")
letter = raw_input("Enter a letter:")
if letter in word:
	print word + " contains the letter " + letter
else:
	print word + " does not contain the letter " + letter