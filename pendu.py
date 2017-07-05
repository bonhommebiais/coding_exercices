import random

import turtle
import sys

# creates a graphics window and a turtle
my_turtle = turtle.Turtle()  
my_drawing = turtle.Screen()

# This function defines the default for the turtle (width of pen, color..)
def init_turtle():	
	my_turtle.width(3)
	my_turtle.color('#00ffff')
	my_drawing.bgcolor('#9400d3')
	my_drawing.setup(450, 450, 700, 50)

init_turtle()

# Draw an horizontal line at the bottom left corner of the drawing window
def step1():
	# The turtle starts by default in middle of drawing window (0,0)
	# We have to move the pen to bottom left window and 
	# lift the pen up so that it does not draw while we move there.
	my_turtle.penup()
	# Retrieve the size of the drawing window
	screen_x, screen_y = my_drawing.screensize()
	# compute the x and y of the bottom left corner
	bottom_left_x = screen_x/2 * -1 + 40
	bottom_left_y = screen_y/2 * -1 + 5
	# position at top left of the drawing window
	my_turtle.setpos(bottom_left_x, bottom_left_y)	
	my_turtle.pendown()
	my_turtle.setheading()
	my_turtle.forward(150) # tell my_turtle to move forward by 150 units# bla

#line up
def step2():
	my_turtle.penup()
	my_turtle.lt(180)
	my_turtle.fd(75)
	my_turtle.rt(90)
	my_turtle.pendown()
	my_turtle.forward(300)

#line across
def step3():
	my_turtle.rt(90)
	my_turtle.fd(150)

#diagonal line
def step4():
	my_turtle.penup()
	my_turtle.lt(180)
	my_turtle.fd(150)
	my_turtle.lt(90)
	my_turtle.fd(50)
	my_turtle.lt(135)
	my_turtle.pendown()
	my_turtle.fd(70.71067811865475)

#rope
def step5():
	my_turtle.penup()
	my_turtle.rt(45)
	my_turtle.fd(100)
	my_turtle.rt(90)
	my_turtle.pendown()
	my_turtle.fd(50)

#head
def step6():
	my_turtle.penup()
	my_turtle.fd(25)
	my_turtle.rt(90)
	my_turtle.fd(25)
	my_turtle.lt(90)
	my_turtle.pendown()
	my_turtle.circle(25, 360)

#body
def step7():
	my_turtle.penup()
	my_turtle.fd(25)
	my_turtle.lt(90)
	my_turtle.fd(25)
	my_turtle.rt(90)
	my_turtle.pendown()
	my_turtle.fd(125)

#left arm
def step8():
	my_turtle.penup()
	my_turtle.rt(180)
	my_turtle.fd(100)
	my_turtle.lt(135)
	my_turtle.pendown()
	my_turtle.fd(60)

#right arm
def step9():
	my_turtle.penup()
	my_turtle.rt(180)
	my_turtle.fd(60)
	my_turtle.rt(90)
	my_turtle.pendown()
	my_turtle.fd(60)

#left leg
def step10():
	my_turtle.penup()
	my_turtle.lt(180)
	my_turtle.fd(60)
	my_turtle.lt(135)
	my_turtle.fd(100)
	my_turtle.rt(45)
	my_turtle.pendown()
	my_turtle.fd(70)

#right leg
def step11():
	my_turtle.penup()
	my_turtle.lt(180)
	my_turtle.fd(70)
	my_turtle.rt(90)
	my_turtle.pendown()
	my_turtle.fd(70)

def draw_step(step_number):
	if step_number == 1:
		step1()
	if step_number == 2:
		step2()
	if step_number == 3:
		step3()
	if step_number == 4:
		step4()
	if step_number == 5:
		step5()
	if step_number == 6:
		step6()
	if step_number == 7:
		step7()
	if step_number == 8:
		step8()
	if step_number == 9:
		step9()
	if step_number == 10:
		step10()
	if step_number == 11:
		step11()

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

def pretty_print(word):

	print " "
	print red("Word to guess:     ") +  blue(" ".join(word))
	print " "

def pretty_list(word):

	print " "
	print blue(" ".join(word)) + red(" is/are not in my word!")
	print " "

# Perform a handman on the word and return True if user wins and false if user fails.
def pendu(word):
	my_turtle.clear()
	blank_word = ["_"] * len(word)
	print " "
	print "Try to find the word i am thinking of."
	pretty_print(blank_word)
	print "________________________________________________________"
	letters_not = []
	lives = 11
	step = 0
	while lives > 0 and blank_word != word:
		print " "
		letter = raw_input ("Guess a letter: ")
		letter = letter.lower()
		if letter in word:
			if letter in blank_word:
				print "You already tried that letter!"
			else:	
				print "You found one!"
				letter_count = 0
				for word_letter in word:
					if letter == word_letter:
						blank_word[letter_count] = word_letter
					letter_count = letter_count + 1
			pretty_print(blank_word)
		else:
			print " "
			print "Try again!"
			print " "
			lives = lives - 1
			step = step + 1
			if letter not in letters_not:
				letters_not.append(letter)
				print "You have " + str(lives) + " lives left!"
			else:
				print "Hey dummy you already tried that letter! ;-)"
				print " "
				print "You have " + str(lives) + " lives left!"
			draw_step(step)
			pretty_list(letters_not)
			pretty_print(blank_word)
		print "________________________________________________________"

	if lives == 0:
		print " "
		print "Yon have no more lives. You lost."
		print " "
		return False
	else:
		print " "
		print "You found it! My word was " + "".join(word) + " ."
		print " "
		return True

def random_pendu(level_words):
	random_word_index = random.randint(0, len(level_words) - 1)
	random_word = level_words[random_word_index]
	return pendu(list(random_word))

print "You need to finish level 1 and to then move on to level 2"

player_result = False
while player_result == False:
	level1_words = ["hand", "with", "none", "cold", "pink", "yawn", "turn", "kill", "jock", "jump", "verb", "kiwi", "peak", "sock", "plum", "wink", "monk", "swim", "lick", "milk", "mash", "dump", "cube", "dude", "dumb", "bake", "fork", "yolk", "poke", "busy", "spec", "pony", "form", "from", "poop", "sync", ""]
	player_result = random_pendu(level1_words)

print "Congratulations you have succeeded Level 1!"

player_result = False
while player_result == False:
	level2_words = ["hello", "first", "dizzy", "crust", "mixed", "child", "pizza", "juice", "quick", "quiet", "unzip", "chock", "hazel", "knock", "froze", "squad", "jello", "puppy", "squid", "black", "shade", "remix", "happy"]
	player_result = random_pendu(level2_words)

print "Congratulations you have succeeded Level 2!"

player_result = False
while player_result == False:
	level3_words = ["onions", "smooth", "poison", "fruity", "soaked", "puzzle"]
	player_result = random_pendu(level3_words)	
	
print " You won all levels"



