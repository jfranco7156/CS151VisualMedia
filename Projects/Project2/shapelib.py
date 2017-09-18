# Jenniber Franco
# CS 151 Fall 2017
# Shape Library
# Uses the turtle to draw a triangle

import turtle as t
import math

# Draws a triangle
def draw_triangle(edge_len):
	""" Draw an equilateral triangle
		Each edge should be edge_len long
	"""
	for x in range(3):
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

# Draws a skylab using block function
def skylab(x,y,size):
	block(-0.5*size+x, -1.5*size+y, 1*size, 3*size)
	block(-1.5*size+x, -0.2*size+y, 1*size, .4*size)
	block(0.5*size+x, -0.2*size+y, 1*size, .4*size)
	block(-2.5*size+x, -3.0*size+y, 1*size, 6*size)
	block(1.5*size+x, -3.0*size+y, 1*size, 6*size)

#Draws an isosceles triangle	
def isotriangle(x,y,sides1,sides2):
	#side1 is the base of the triangle
	goto(x,y)
	base = sides1/2
	angle2 = math.degrees(math.acos(base/sides2))#angle of the two sides on the base
	angle1 = 180 - (2*angle2)#angle of the vertex
	t.forward(sides1)
	t.left(180-angle2)
	t.forward(sides2)
	t.left(180-angle1)
	t.forward(sides2)
	t.left(180-angle2)
		
#Draws a pentagon
def pentagon(x,y,len):
	goto(x,y)
	for i in range(5):
		t.forward(len)
		t.right(72)

#Draws a star using the pentagon and triangle function
def star(x,y,center_len, sides):
	pentagon(x,y,center_len)
	isotriangle(x,y,center_len, sides)
	t.right(72)
	x= x+center_len
	isotriangle(x,y,center_len, sides)
	t.right(72)
	isotriangle(x,y,center_len, sides)
	isotriangle(x,y,center_len, sides)
	isotriangle(x,y,center_len, sides)
		
def draw_star(size, color):
	angle = 120
	for side in range(5):
		t.forward(size)
		t.right(angle)
		t.forward(size)
		t.right(72 - angle)

















