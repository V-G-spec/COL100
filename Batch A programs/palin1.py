def rev(x):
    y=0
    while x>0:
        y=y*10+x%10
        x=x//10
    return y
def palindrome():
    k=0
    for i in range(1000,9999):
        for j in range(1000, 9999):
            if (i*j) == rev(i*j):
              if(i*j)>k:
                k=i*j
    print(k)
palindrome()
