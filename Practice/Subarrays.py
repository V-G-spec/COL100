# [1,2,3] = [1],[2],[3],[1,2],[2,3],[1,3]
def subset(ar):
	a=[]
	for i in ar:
		a.append([i])
		k=len(a)
		for j in range(k-1):
			if a[j]!=[i]:
				r=[*a[j],i]
				a.append(r)
	print(a,"\n",len(a))



def displaysublist(A): 
   # store all the sublists  
   B = [[ ]] 
      
   # first loop  
   for i in range(len(A) + 1):   
      # second loop  
      for j in range(i + 1, len(A) + 1):         
         # slice the subarray  
         sub = A[i:j] 
         B.append(sub) 
   return B

print(displaysublist([1,2,3,4]))


def subarray(ar):
	a=[]
	for i in ar:
		a.append([i])	
		k=len(a)
		for j in range(k-1):
			if a[j]!=[i]:
				r=[*a[j],i]
				a.append(r)
	print(a,"\n",len(a))