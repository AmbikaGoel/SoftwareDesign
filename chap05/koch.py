from swampy.TurtleWorld import*

world = TurtleWorld()
bob = Turtle ()
bob.delay=.001
print bob
angle=60

def koch(t, depth):
	if depth<3:
	    fd(t, depth)
	    return
	m = depth/3.0
	koch(t, m)
	lt(t, angle)
	koch(t, m)
	rt(t, angle*2)
	koch(t, m)
	lt(t, angle)
	koch(t, m)
def snowflake(t,depth):
	for i in range (3):
		koch(t,depth)
		rt(t,angle*2)
				
snowflake(bob,100)