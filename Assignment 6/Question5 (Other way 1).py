import copy
def subtract_lists(a,b):
    """Subtracts 2 arrays, given that number stored in a>= number stored in b. Otherwie, it reutns 0"""
    l=copy.deepcopy(a) #to avoid changes in original array
    m=copy.deepcopy(b)
    while(l[0]==0): #To remove any redundant zeroes in front
        l.pop(0)
        if len(l)==0: #If l is an empty array, assign it value 0
            l.append(0)
            break
    while(m[0]==0): ##To remove any redundant zeroes in front
        m.pop(0)
        if len(m) == 0: #If m is an empty array, assign it value 0
            m.append(0)
            break
    x=len(l)
    y=len(m)
    if x==y:
        for i in range(x): #To return 0 if for divisor and dividend of same length, dividend<divisor
            if l[i]<m[i]:
                return [0]
            elif l[i] == m[i]:
                continue
            else:
                break
    elif x<y:
        return [0] #if number of digits in dividend<number of divisors in divisor, return 0
    c=[]
    l.insert(0,0) #append 0 in front of the dividend for terminal condition in subtraction
    m.insert(0,0) #append 0 in front of the divisor for terminal condition in subtraction
    for i in range(1,x-y+1): #ADding redundatn 0s, so that length of l and m is same
        m.insert(0,0) #insert(x,y) implies insert y at x th position (This was for self clarification and not an assertion)
    for i in range(x):
        #grade school multiplication, Proof was part of Assignment-5
        if l[-1-i]<m[-1-i]:
            c.insert(0,10+l[-1-i]-m[-1-i])
            l[-2-i]-=1
        else:
            c.insert(0,l[-1-i]-m[-1-i])
    return c


def division(dividend,divisor):
    """Division by repeated subtraction on the whole arrays"""
    if divisor==[0]:
        return "Nope, not possible. Imagine dividing 0 slices of Pizza among your 0 friends. Sad, isn't it?"
    val=0
    while(subtract_lists(dividend,divisor)!=[0]):
        dividend=subtract_lists(dividend,divisor)
        val+=1
    if dividend==divisor:
        dividend=[0]
        val+=1
    return (val,dividend)

print(division([9,6],[2]))
