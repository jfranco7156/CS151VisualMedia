# Jenniber Franco
# Fall 2017
# Project 6
# Test Python File

import time
import random
import graphicsPlus as gr

def main():
	win = gr.GraphWin("Testing",500,500,False)
	
	shapes  = []
	
	c = gr.Circle(gr.Point(250,250),10)
	c.draw(win)
	shapes.append(c)
	
	while True:
		time.sleep(0.5)
		for thing in shapes:
			r = 100 + random.randint(0,155)
			g = 80 + random.randint(0,100)
			b = random.randint(10,80)
			
			thing.setFill(gr.color_rgb(r,g,b))
			thing.setOutline(gr.color_rgb(r,g,b))
			
			dx = random.randint(-10,10)
			dy = random.randint(-10,10)
			thing.move(dx,dy)
		
		if random.random() < 0.2:
			oldthing = random.choice(shapes)
			newthing = oldthing.clone()
			newthing.draw(win)
			shapes.append(newthing)
		
		win.update()
		
		if win.checkMouse() != None:
			break
			
	win.close()
	
	
if __name__ == "__main__":
	main()