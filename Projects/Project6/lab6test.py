# Bruce Maxwell
# originally written in fall 2012
#

import time
import graphics as gr
import complex_shape as cs

def saveFrame( basename, win, frame ):
    win.postscript( file="%s_%000d.ps"%(basename,frame), colormode='color')

def main():
    """ creates a scene with several animated spaceships"""
    # create a window
    win = gr.GraphWin( 'Spaceships', 600, 600, False )

    # create three spaceships
    sp1 = cs.spaceship_init( 100, 500, 2.0 )
    sp2 = cs.spaceship_init( 300, 200, 0.4 )
    sp3 = cs.spaceship_init( 400, 300, 1.0 )

    # put all the spaceship objects in a list
    spaceships = [sp1, sp2, sp3]

    # draw all the spaceships
    for ship in spaceships:
        cs.draw( ship, win )
    
    # loop until the user clicks
    t = 0
    while True:
        time.sleep(0.25)

        # loop over the spaceship objects and animate them
        for ship in spaceships:
            cs.spaceship_animate( ship, t, win )

        # increment the frame counter
        t += 1
        
        # Update the display
        win.update()
        
        # save the frames by uncommenting the following line
        # saveFrame( 'lab6testmovie', win, t )

        # check for a mouse event and break if it occurs
        if win.checkMouse():
            break

    # close the window
    win.close()

if __name__ == "__main__":
    main()

        
