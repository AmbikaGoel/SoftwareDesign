from swampy.TurtleWorld import*
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def square(bob,length):
	for i in range (4):
		fd(bob, length)
		lt(bob)
#square(bob,1000)

def polygon(t,n,length):
	angle = 360.0 / n
	for i in range (n):
		fd(t, length)
		lt(t, angle)
#polygon(bob,180,1)

def circle(t,r):
	circumfrence = 2*3.14*r
	n=20
	polygon (t,n,circumfrence/n)
#circle(bob,20)

def arc(t,r,angle):
	arclength = 2*math.pi*r*angle/360
	n = int (arclength/3) + 1
	steplength = arclength/n
	stepangle = angle/n
	for i in range (n):
		fd(t, steplength)
		lt(t, stepangle)
arc(bob,50,180)

