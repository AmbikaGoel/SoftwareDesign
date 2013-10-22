from swampy.TurtleWorld import*

world = TurtleWorld()
bob = Turtle ()
bob.delay=.001
print bob
length=10

def curve(t, depth,angle):
	if depth<3:
		return
	m=depth/3
	rt(t, angle)
	curve(t, depth/3,-angle)
	fd(t, length)
	lt(t, angle)
	curve(t, depth/3,angle)
	fd(t, length)
	curve(t, depth/3,angle)
	lt(t, angle)
	fd(t, length)
	curve(t, depth/3,-angle)
	rt(t, angle)
curve(bob, 100, 90)