def prime(n):
	i=3
	flag=False
	while (i*i<n):
		if (n % i)==0:
			flag=True
			break
		i+=2
	if (n==2) or (n%2==1 and flag==False):
		print("The number is prime")
	else:
		print("The number is not prime")
prime(int(input("Enter a number: ")))
	
