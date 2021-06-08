### Answer 1 Bonus ###

def mul(a,b):
	#assert: len(a)>len(b)
	if a[-1]==0 or b[-1]==0:
		return [0]
	else:	

		a.insert(0,0)
		c=[0]*(len(a))
		#INV: calculation from LSB. After kth iteration, last k digits of the sum of the 2 numbers will be stored in c
		for i in range(len(b)):
			c[-i-1]=(a[-1-i]*b[-1-i])%10
			carry=(a[-1-i]*b[-1-i])//10
			a[-2-i]+=carry
		i+=1
		while(i<len(a)-1):
			c[-i-1]=(a[-i-1]%10)
			a[-i-2]+=a[-i-1]//10
			i+=1
		c[0]=a[0]
		if c[0]==0:
			c.pop(0)
		return c

print(add2([1,9,3,4],[9,8]))



	