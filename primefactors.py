def get_prime_factors(n):
	factors = list()
	for i in range(1,n):
		x=n%i
		if(x==0):
			factors.append(i)
		else:
			i=i+1
	print(factors)

get_prime_factors(7986)
