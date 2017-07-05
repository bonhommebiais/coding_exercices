word = raw_input("Enter a word: ")
vowels = ["a", "e", "i", "o", "u", "y"]
while word:
	consonants = []
	vowels_word = []
	for letter in word:
		if letter in vowels:
			vowels_word.append(letter)
		else:
			consonants.append(letter) 
	print "Vowel(s): " + str(vowels_word)
	print "Consonant(s): " + str(consonants)
	word = raw_input("Enter a word: ")
print "See ya!"
