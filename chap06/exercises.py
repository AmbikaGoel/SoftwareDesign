def is_power(a,b):
	if a%b==0:
		print True
	else:
		print False
print is_power(14,4)


def gcd(a,b):
	if b==0:
		print a
	else:
		return gcd(b,a%b)

print gcd(1071,462)
