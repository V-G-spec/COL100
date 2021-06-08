n=int(input("please enter a number : "))
count=0
while n>0:
    n=n//2
    count=count+1
print(2**(count-1),2**count)
