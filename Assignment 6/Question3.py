def partition(a,l,r):
    #assert: Previous proof but partitions between l and r
    # It considers the first element as a pivot and moves all smaller element to left of it and greater elements to right
    x=a[l]
    n=len(a)
    i=l
    j=r
    while(i<j):
        if a[i]>=x and a[j]<=x:
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1
        elif a[i]<x:
            i+=1
        else:
            j-=1
    return(a,i)

def kth(a,l,r,k):
    if (k>0 and k<= r-l+1):
        # Partition the array around last element and get position of the pivot element in partioned array
        (array,pos_i)=partition(a,l,r)

        # if position is same as k
        if (pos_i-l==k-1):
            return a[pos_i]
        # If position is more then k, apply recursion for left sub array
        if (pos_i-l>k-1):
            return kth(a,l,pos_i-1,k)
        else: #apply recursion for the right sub array
            return kth(a,pos_i+1,r,k-pos_i+l-1)
    else:
        return ": Seriously? Imagine asking for 7th biggest slice of pizza with 6 pieces"

arr = [12, 3, 5, 7, 4, 19, 26]
n = len(arr)
k = 2;
print(k,"th smallest element is",kth(arr, 0, n - 1, k))

#Time Complexity:
#The time comlpexity depends upon the pivot chosen
#If the pivot decreases size of array by 1 element (Worst case) the time complexity is O(n^2)
#If the pivot decreases size of array by some fraction (Maybe n/2) (Best case) the time complexity is O(n) (=n/2+n/4+n/8+.... < n)
