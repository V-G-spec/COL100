a=int(input("please enter a number : "))
b=int(input("please enter a number : "))
c=int(input("please enter a number : "))
count=0
if a>b and a>c and b>c:
    print(b)
elif b>a and b>c and a>c:
    print(a)
elif c>a and c>b and b>a:
   print(b)
elif b>a and b>a and c>a:
    print(c)
elif c>a and c>b and a>b:
    print(a)
elif a>c and a>b and c>b:
    print(c)
elif a==b==c:
    print(a)
elif a==b: 
    print(a)
elif a==c: 
    print(a)
elif b==c: 
    print(b)
    
