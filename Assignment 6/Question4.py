def lms(a):
    #INV: after the ith iteration, find length of longest monotonic subsequence till ith element of the array"""
    n=len(a)
    maxi=[]
    for i in range(n):
        maxi.append(1) #initiate a matrix with all elements as 1 because even if all numbers are sorted in descending order in given array, length of longest monotonix subsequence till that element wiuld be 1 (that elementitself)
    i=1
    while(i<n):
        for j in range(i): # j varies from 0 to i
            if a[i]>a[j]: #if ith element > jth element, the last term of that subsequence would now be i
                maxi[i]=max(maxi[j]+1,maxi[i]) #Since we have to find length of longest to the point, we check if by some other path the length of longest monotonic subsequence is not already more
        i+=1
    return max(maxi)

print("The size of largest monotonic subsequence is:",lms([1,9,6,2,9,4,7,3,11,8,14,16]))

#Time complexity:
#T(n)=Σ(i-1) + c = n(n-1)/2 - n + c = n(n-3)/2= O(n^2)
