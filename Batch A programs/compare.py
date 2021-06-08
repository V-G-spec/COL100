a=[2,3,4]
b=[1,5,3]

def compareTriplets(a, b):
    x=0
    y=0
    for i in range(2):
        if a[i]<b[i]:
            y=y+1
        elif a[i]>b[i]:
            x=x+1
    return x,y   
print(compareTriplets(a, b))
