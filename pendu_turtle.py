

#!/usr/bin/python

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
	my_drawing.setup(450, 450, -100, 25)

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
		init_turtle()
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

def dessin():
	init_turtle()
	step1()
	step2()
	step3()
	step4()
	step5()
	step6()
	step7()
	step8()
	step9()
	step10()
	step11()
	my_drawing.exitonclick()

print 'hello'
sys.stdout.flush()
dessin()
myturtle.py
Ouvrir avec Google Docs
Affichage de myturtle.py en cours...