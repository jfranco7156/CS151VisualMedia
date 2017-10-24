# Jenniber Franco
# CS 151 Fall 2017
# Main File - Project 2

import shapelib as s

# Draws a telescope
def space1(x,y,width,height):
	for i in range(3):
		s.block(x,y,width,height)
		x = x + width
		y = y - (height/4)
		width -= 20
		height -= 15

#s.t.color("blue")		
#s.isotriangle(20,20,60,100)
#s.t.color("red")
#s.pentagon(100,100,60)

#s.draw_star(25,'blue')

space1(50,50,75,100)

input("Enter")