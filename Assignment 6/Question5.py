import copy
def subtract_lists(a,b):
    """Subtracts 2 arrays, given that number stored in a>= number stored in b. Otherwie, it reutns 0"""
    l=copy.deepcopy(a) #to avoid changes in original array
    m=copy.deepcopy(b)
    while(l[0]==0): #To remove any redundant zeroes in front
        l.pop(0)
        if len(l)==0: #If l is an empty array, assign it value 0
            l=[0]
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



def checkzero(a):
    """Checks if the given array has all elements as 0"""
    b=copy.deepcopy(a) #To avoid changes in original matrix
    k=[]
    if b==k:
        return True
    elif b[0]==0:
        b.pop(0)
        return(checkzero(b))
    else:
        return False


def division(dividend,divisor):
    """Lezz divide it"""
    rem=[] #intialize Remainder
    quo=[] #intialize Quotient
    if checkzero(divisor): #Division by 0 isn't possible
        return "Seriously? Try dividing some cookies among your 0 friends. Sucks, right?";
    elif checkzero(dividend):
        quo=[0]; rem=[0]
        return (quo,rem)
    else:
        for i in range(len(dividend)): #Invariant: at ith iteration we know Quotient and Remainder for dividend=dividend[:i+1] and divisor
            val=0
            rem.append(dividend[i]) #In each iteration, it adds a digit from the dividend, just like long division
            while(checkzero(subtract_lists(divisor,rem))): #checks if divisor<Remainder to get highest multiple of divisor less than dividend
                val+=1 #to evaluate the val^th multiple of divisor
                rem=subtract_lists(rem,divisor)
            quo.append(val)
        return (quo,rem)

dividend=[7,5,5,0]
divisor=[2,5]

print(dividend,"/",divisor,"==>Quotient and Remainder:",division(dividend,divisor))

#Time Complexity:
#Worst Case:
#let n be size of max(dividend and divisor). The division function has n iterations with one assertion calling the subtraction function which again requires n iterations
#Time Complexity=O(n^2)









###Other Way-1 for Question 5


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






###Other Way 2 for Question 5

def to_int(a):
    """Covert array to int"""
    val=0
    for i in range(len(a)):
        val=val*10+a[i]
    return val
def to_array(n):
    """Covert int to array"""
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
