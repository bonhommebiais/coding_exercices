#!/usr/bin/python

# This function print in blue the string passed as argument.
def blue(word):
	blue_begin = u'\u001b[0;34m'
  	blue_end = u'\u001b[0m'
  	return blue_begin + word + blue_end

# This function print in red the string passed as argument.
def red(word):
	red_begin = u'\u001b[0;31m'
  	red_end = u'\u001b[0m'
  	return red_begin + word + red_end

# This function nicely prints the list of character words
def pretty_print(word):

	print " "
	print red("Word to guess:     ") +  blue(" ".join(word))
	print " "

word_to_guess = ["_", "_", "T", "_", "T"]
pretty_print(word_to_guess)

