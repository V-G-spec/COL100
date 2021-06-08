def partition(a,x):
    #assert: a[left..right] is established and x is the partition value
    n=len(a)
    i=0
    j=n-1
    #INV: after i iterations, (lower <= upper) ^ (lower = i) ^ (upper = n - 1 - i) ^ (all l[0,...lower - 1] <= x, all l[upper + 1, len(l) - 1] >= x)
    while(i<j):
        if a[i]>=x and a[j]<=x:
            a[i],a[j]=a[j],a[i]     #assert: Exchange the wrongly partitioned pair
            i+=1
            j-=1
            #assert: Extend both partitions inward by one element
        elif a[i]<x:
            i+=1    #assert:Extend the left partition while elements are less than or equal to x
        else:
            j-=1    #assert:Extend the right partition while elements are greater than x
    return(a,i)
    #assert: a is the new partitioned array and i is the partition index st a[i]<x<a[i+1]

arr=[28,26,25,11,16,12,24,29,6,10]
print(arr)
(x,y)=(partition(arr,17))
print("Partitioned Array: ",x,"\n Partition index: ",y)

#Time Complexity:
#Worst case time complexity is when element to be partitioned about is greater than/smaller than every element in the array in which case it will be O(n)
#Best case time complexity is when array is already partitioned in which case it will be O(n/2)
#We know that for any general array/element number of values attained by i + number of values attained by j = n and n-1>i,j>0
