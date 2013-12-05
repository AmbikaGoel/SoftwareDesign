"""Solution to an exercise in Think Python."""

"Author:"
"Ambika Goel"

def grid(a,b,c,d,g,l): 
	e=c+((b+c)*g)+a # prints ' - - - - - +'
	f=c*(g*2+1)+d	# prints '           |'
	h='\n'		# starts new line
	i=a+e*2		# prints'+ - - - - - - + - - - - - - +'
	j=d+f*2		# prints '|             |             |'
	k=i+(h+j)*(l)+h # prints line i, then line j (l) times (basically top 1/2 				  of box)
	print (k)*2+i
grid('+','-',' ','|',1,1)
