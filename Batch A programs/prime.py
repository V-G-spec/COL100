n=int(input("please enter a number : "))
count=0
for i in range(1,n):
    if n%i==0:
        count=count+1
        i=i+1
if count>1:
    print("input number is composite")
else:
    print("input number is prime")
        
    
