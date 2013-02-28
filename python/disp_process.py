import psutil
import curses 
from time import sleep

print dir(psutil)
print dir(curses)


def setup():
	return curses.initscr()

def p(x, y):
	return curses.newpad(x,y)

def teardown():
	curses.nocbreak()
	stdscr.keypad(0)
	curses.echo()

def end():
	curses.endwin()

if __name__ == "__main__":
	stdscr = setup()
	pad = p(100, 100)
	#  These loops fill the pad with letters; this is
	# explained in the next section
	for y in range(0, 100):
		for x in range(0, 100):
			try: pad.addch(y,x, ord('a') + (x*x+y*y) % 26 )
			except curses.error: pass

	#  Displays a section of the pad in the middle of the screen
	pad.refresh( 0,0, 5,5, 20,75)

	#curses.nocbreak(); stdscr.keypad(0); curses.echo()
	sleep(10)
	teardown()
	end()
