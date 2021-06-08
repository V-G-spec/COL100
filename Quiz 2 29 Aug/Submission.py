### Answer 2 ###


import random

def swap(ar,a,b): #Swap elements at 2 positions "a" and "b" of a an array "ar"
	temp=ar[a]
	ar[a]=ar[b]
	ar[b]=temp

def arrange(ar):
	#assert: ar is a well established array containing only 3 unique elements 1,2,3 
	lower=0
	upper=len(ar)-1
	ite_r=len(ar)-1 #The iterating variable

	while ite_r>=lower:
		#INV: (After any iteration, ar[0...lower] take the value 1, ar[upper...len(ar)-1] are all 3) ^ (lower<=ite_r<=len(ar)-1)
		# Once the loop is terminated, all 1's in the original array end up at the start and 3's in the end. Subsequently, the remaining numbers i.e. all the 2's, are in the middle
		
		if ar[ite_r]==1:
			# swap if the element at iterator is 1 with the element at the postion "lower" s.t. every element till lower is 1
			# increase value of lower by 1
			swap(ar,ite_r,lower)
			lower+=1

		elif ar[ite_r]==3:
			# swap if the element at iterator is 3 with the element at the postion "upper" s.t. every element after upper is 3
			# decrease value of upper and ite_r by 1
			swap(ar,ite_r,upper)
			upper=upper-1
			ite_r-=1

		elif ar[ite_r]==2:
			ite_r-=1
	return ar

# a=[2,3,3,2,3,3,1,2]
a=random.sample(range(1,4), 3)+random.sample(range(1,4), 2)+random.sample(range(1,4), 1)+random.sample(range(1,4), 3)+random.sample(range(1,4), 2)
print(a)
print(arrange(a))




### Answer 3 ###

#Any number in such an array can only be represented as 2^a*3^b*5^c where a,b,c>=0. Therefore, we check prime factors of every number and if they are other than 2,3,5; we discard them


def primefac(n): 
    """Store prime factors of a number in a list"""
    l=[]
    # Store the number of two's that divide n 
    while n % 2 == 0: 
        l.append(2), 
        n = n / 2
          
    # Now n is odd
    # We can skip multiples of 2 
    for i in range(3,int(n**(0.5))+1,2): 
          
        # while i divides n , store i in l and divide n 
        while n % i== 0: 
            l.append(i), 
            n = n / i 
              
    # Last condition: if n is a prime 
    # and number greater than 2 
    if n > 2: 
        l.append(n)
    return l

def check(k):
	"""Check if the prime factors of a number only constitute of 2,3,5 or not"""
	out=primefac(k)
	flag=True
	for i in out:
		if (i!=2) and (i!=3) and (i!=5): #If prime factor is not 2,3 or 5 it means that it is divisble by some other prime factor
			flag=False
			break
	return flag
	

def divopr(n):
	#INV: at the ith iteration we have checked if the integer i is divisible by any prime other than 2,3,5. If it is not, we tore it in the output list, arr
	arr=[]
	cur_num=1
	while len(arr)<n:
		#Loop terminates when we have a sorted list of N integers such that none of the elements is divisble by any number other than 2,3 or 5
		if check(cur_num):
			arr.append(cur_num)
		cur_num+=1
	return arr

print(divopr(150))



