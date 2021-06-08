a=input("please enter a word : ")
b=input("please enter a word : ")
count=0

for i in range(0,len(a)):
    for j in range(0,len(b)):
        if a[i]==b[j]:
            count=count+1
            break
        else:
            count=count

print(count)
    
