def to_int(a):
    val=0
    for i in range(len(a)):
        val=val*10+a[i]
    return val
def to_array(n):
    a=[]
    while(n!=0):
        a.insert(-1,n%10)
        n=n//10
    return a


def division(dividend,divisor):
    """Simply convert array to integer and perform division and convert them back to arrays"""
    div=to_int(dividend)
    divi=to_int(divisor)
    if (divi==0):
        print("Nope, not possible. Imagine dividing 0 slices of Pizza among your 0 friends. Sad, isn't it?")
    else:
        print("The Quotient is:",to_array(div//divi),"The Remainder is:",to_array(div%divi))
division([3,7,1],[0])
