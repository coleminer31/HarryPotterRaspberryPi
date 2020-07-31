# adapted from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py
# and https://www.jonwitts.co.uk/archives/896
 
import sys, termios, tty, os, time
from pivotpi import *
import numpy as np

# begin part found on https://www.jonwitts.co.uk/archives/896

#define the get char function 
def getch():
    
    fd = sys.stdin.fileno()
    
    old_settings = termios.tcgetattr(fd)
    
    try:
        
        tty.setraw(sys.stdin.fileno())
        
        ch = sys.stdin.read(1)
 
    finally:
        
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        
    return ch

# end part found on https://www.jonwitts.co.uk/archives/896

# make this the character you set for certain wand motions on the FLIRC
YOUR_LETTER_HERE = 'PUT YOUR CHOSEN CHARACTER HERE'

#START THE MAGIC WHILE LOOP

while True:

	#try to get a char from the keyboard
	try:

	    #get the keyboard press
	    char = getch()
	 
	    #check to see if the char is "o" (open)
	    if (char == YOUR_LETTER_HERE):
	        
		#DO SOMETHING HERE

	#if you don't get a char from the keyboard, pass to the next iteration
	except:

		#move on to the next iteration of the while loop
		pass

# END THE MAGIC WHILE LOOP
