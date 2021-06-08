def remdup(a):
    #assert: a[0..-1] is established with r as the size of this matrix that is a constant
    n=len(a)
    r=len(a)
    i=0;
    while(i<n):
        j=i+1
        while(j<n):
            if (a[i]==a[j]):
                a.pop(j)
                a.append(0)
                n-=1
                #INV: After ith iteration, all elements in a[0..i+1] are unique
                #assert: a[n..r-1] are all zeroes
            else:
                break

        i+=1
    #assert: a is the new array with duplicates removed and n is the new size
    return (a,n)


arr=[0,0,1,2,2,2,7,8,8,9,9,9,9,11,11,11,11,12,13,14,15,15,16,16,16,16,16,16,16,16,17,18,20,20,20];
print("\t The array is: ",arr)
(arr,y)=remdup(arr)
print("\t The new array is: ",arr,"\n \t The new size is: ",y)

#Time Complexity:
#Worst case time complexity is when all elements are same in which case after all iterations of j for i=0, n will be equal to 1. Therefore time complexity is O(n)
#Best case is when all elements are different, j will only get 1 value for any i and therefore the time complexity is O(n)
#Hence the time complexity of given algorithm is O(n)
