# Jenniber Franco
# Fall 2017
# Project 6
# Complex Shape

import time
import random
import graphicsPlus as gr

def draw( objlist, win ):
	""" Draw all of the objects in objlist in the window (win) """
	for thing in objlist:
		thing.draw(win)

def move( objlist, dx, dy ):
	""" Draw all of the objects in objlist by dx in the x-direction
	and dy in the y-direction """
	for item in objlist:
		item.move(dx,dy)

def undraw( objlist ):
	""" Undraw all of the objects in objlist """
	for thing in objlist:
		thing.undraw()

def spaceship_init( x, y, scale ):
	'''Creates and returns a list of graphics objects to make up a spaceship'''
	
	shapes = []
	
	# Body of the rocket
	r = gr.Rectangle(gr.Point(x-scale*10,y),gr.Point(x+scale*10,y-scale*80))
	r.setFill(gr.color_rgb(185,185,185))
	shapes.append(r)
	
	# Nose of the rocket
	p1 = gr.Polygon(gr.Point(x-scale*10,y-scale*80),gr.Point(x,y-scale*100),gr.Point(x+scale*10,y-scale*80))
	p1.setFill(gr.color_rgb(150,170,200))
	shapes.append(p1)
	
	# Left fin of the rocket
	p2 = gr.Polygon(gr.Point(x-scale*10,y), gr.Point(x-scale*10,y-scale*20),gr.Point(x-scale*25,y))
	p2.setFill(gr.color_rgb(200,170,150))
	shapes.append(p2)

	# Right fin of the rocket
	p3 = gr.Polygon(gr.Point(x+scale*10,y), gr.Point(x+scale*10,y-scale*20),gr.Point(x+scale*25,y))
	p3.setFill(gr.color_rgb(200,170,150))
	shapes.append(p3)
	
	return shapes


def pumpkin_init(x,y,scale):
	
	"""Makes a list of graphic objects to draw a pumpkin with a face"""
	shapes = []
	inOrange = gr.color_rgb(251,161,52)

	#Face of the pumpkin
	face = gr.Oval(gr.Point(x-scale*40,y-scale*25),gr.Point(x+scale*40,y+scale*25))
	face.setFill(gr.color_rgb(205,108,41))
	shapes.append(face)

	#Eyes of Pumpkin
	eye1 = gr.Polygon(gr.Point(x-scale*12,y-scale*18),gr.Point(x-scale*18,y-scale*5),gr.Point(x-scale*8,y-scale*5))
	eye1.setFill(inOrange)
	shapes.append(eye1)
	
	eye2 = gr.Polygon(gr.Point(x+scale*12,y-scale*18),gr.Point(x+scale*18,y-scale*5),gr.Point(x+scale*8,y-scale*5))
	eye2.setFill(inOrange)
	shapes.append(eye2)
	
	#Draws the nose
	nose = gr.Polygon(gr.Point(x,y-scale*5),gr.Point(x-scale*5,y+scale*5),gr.Point(x+scale*5,y+scale*5))
	nose.setFill(inOrange)
	shapes.append(nose)

	#Draw the mouth
	mouth = gr.Polygon(gr.Point(x-scale*20,y+scale*10),gr.Point(x-scale*10,y+scale*18),gr.Point(x+scale*10,y+scale*18),gr.Point(x+scale*20,y+scale*10))
	mouth.setFill(inOrange)
	shapes.append(mouth)

	return shapes

def house_init(x,y,scale):
	shapes = []

	#Roof of the house
	roof = gr.Polygon(gr.Point(x,y),gr.Point(x,y),gr.Point(x,y))
	shapes.append(roof)

	#Main Body of the House
	body = gr.Rectangle(gr.Point(x-scale*100,y-scale*50),gr.Point(x+scale*100,y+scale*50))
	shapes.append(body)

	#Windows of the House
	window1 = gr.Rectangle(gr.Point(x-scale*75,y-scale*40),gr.Point(x-scale*45,y-scale*10))
	shapes.append(window1)

	window2 = window1.clone()
	window2.move(120,0)

	#Door of the House
	door = gr.Rectangle(gr.Point(x-scale*20,y-scale*10),gr.Point(x+scale*20,y+scale*50))
	shapes.append(door)

	return shapes

def spaceship_animate( shapes, win ):
	'''given the spaceship list, a frame number, and a window, move the spaceship as appropriate'''
	
	p1 = shapes[0].getP1()
	p2 = shapes[0].getP2()
	
	dx = p2.getX()-p1.getX()
	
	newx = (p2.getX()+p1.getX())//2
	newy = p1.getY()
	
	for j in range(0,2):
		c = gr.Circle(gr.Point(newx,newy),0.4*dx)
		c.setFill(gr.color_rgb(250,250,200))
		c.draw(win)
		shapes.append(c)
		
	for item in shapes[0:4]:
		item.move(0,-dx*0.25)
		
	count = 4
	for item in shapes[4:]:
		c = item.getCenter()
		
		if c.getY() < p1.getY()+ 5*dx:
			if count%2 == 0:
				item.move(random.randint(-10,0),dx*0.5)
			else:
				item.move(random.randint(0,10),dx*0.5)
		else:
			item.undraw()
			shapes.pop(count)
			count -= 1
		count += 1

def pumpkin_animate(shapes, frame_num, win):
	"""given the list of items in the shapes and dependent on the numvber"""
	cList = [gr.color_rgb(251,161,52),gr.color_rgb(254,186,86),gr.color_rgb(255,199,119)]
	color = frame_num%len(cList)
	for item in shapes[1:]:
		item.setFill(cList[color])

	
def test_spaceship():
	'''Create a window, draw the spaceship into the window'''
	win = gr.GraphWin( 'Spaceship', 500, 400, False )

	# initialize the spaceship list
	spaceship = spaceship_init(250, 300, 1.0)

	# draw the items into the window
	"""for item in spaceship:
		item.draw( win )"""
	draw(spaceship,win)
	
	for frame_num in range(100):
		time.sleep( 0.25 )
		spaceship_animate( spaceship, win )
		win.update()
		if win.checkMouse():
			break
			
	win.getMouse()
	win.close()

def test_pumpkin():
	'''Create a window, draw the pumpkin into the window'''
	win = gr.GraphWin( 'Pumpkin', 500, 400, False )

	# initialize the spaceship list
	pumpkin = pumpkin_init(100,150,2.0)

	# draw the items into the window
	draw(pumpkin,win)

	for frame_num in range(100):
		time.sleep(0.25)
		pumpkin_animate(pumpkin,frame_num,win)
		win.update()
		if win.checkMouse():
			break
	
	win.getMouse()
	win.close()

def test_house():
	'''Create a window, draw the house into the window'''
	win = gr.GraphWin( 'House', 500, 400, False )

	# initialize the spaceship list
	house = house_init(100,150,2.0)

	# draw the items into the window
	draw(house,win)
	
	win.getMouse()
	win.close()


if __name__ == "__main__":
	test_house()