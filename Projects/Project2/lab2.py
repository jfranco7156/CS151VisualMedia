# Jenniber Franco
# CS 151 Fall 2017
# Shape Library
# Uses the turtle to draw a triangle

import turtle as t
import random

# Draws a triangle
def draw_triangle(edge_len):
	""" Draw an equilateral triangle
		Each edge should be edge_len long
	"""
	for x in range(0,3):
		t.forward(edge_len)
		t.left(120)
		
def block(x,y,w,h,):
	'''Draws a block at (x, y) of the given width and height'''
	goto( x, y )
	for i in range(2):
		# tell the turtle to go foward by width
		t.forward(w)
		# tell the turtle to turn left by 90 degrees
		t.left(90)
		# tell the turtle to go forward by height
		t.forward(h)
		# tell the turtle to turn left by 90 degrees
		t.left(90)
	print('block(): drawing block of size', w, h)

# Moves the turtle to (x,y) without drawing
def goto(x,y):
	t.up()
	t.goto(x,y)
	t.down()
	
def skylab(x,y,size):
	block(-0.5*size+x, -1.5*size+y, 1*size, 3*size)
	block(-1.5*size+x, -0.2*size+y, 1*size, .4*size)
	block(0.5*size+x, -0.2*size+y, 1*size, .4*size)
	block(-2.5*size+x, -3.0*size+y, 1*size, 6*size)
	block(1.5*size+x, -3.0*size+y, 1*size, 6*size)

"""
# main code
draw_triangle(50)
draw_triangle(100)"""

#goto(100,-100)
#t.forward(100)
#goto(-200,0)
#t.forward(100)

block(0,0,100,200)
block(20,20,60,160)

"""t.tracer(False)
for i  in range(200):
	rx = random.randint(-250,250)
	ry = random.randint(-250,250)
	rscale = 5 + random.random() * 15
	r = random.random()
	g = random.random()
	b = random.random()
	t.color(r,g,b)
	
	skylab(rx,ry,rscale)

t.update()
"""

input("Enter")