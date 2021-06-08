word=str(input("please enter a word : "))
for t in range(0,len(word)):
    if word[t]=='e':
        word = word[0:t]+"i"+word[t+1:len(word)]
print(word)
