from swampy.TurtleWorld import*

world = TurtleWorld()
bob = Turtle ()
bob.delay=.001
print bob
angle=60

def koch(t, n):
	if n<3:
	    fd(t, n)
	    return
	m = n/3.0
	koch(t, m)
	lt(t, angle)
	koch(t, m)
	rt(t, angle*2)
	koch(t, m)
	lt(t, angle)
	koch(t, m)
def snowflake(t,n):
	for i in range (3):
		koch(t,n)
		rt(t,angle*2)
				
snowflake(bob,100)