def is_power(a,b):
	if a%b==0:
		is_power(a/b,b)
		return True
	else:
		return False
print is_power(4,16) #should be False
print is_power (8,4) #should be True

def gcd(a,b):
	if a>b:
		r=a%b
		if r==0:
			return b
		else:
			return gcd (b,r)
	if a<b:
		r=b%a
		if r==0:
			return a
		else:
	 		return gcd (a,r)
print gcd(147,105)

