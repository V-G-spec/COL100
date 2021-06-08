sentence = str(input("please enter a sentence : "))
count = 0

def count_space_start(string):
    p = len(string)
    for var in range(p):
        if string[var] == " ":
            break
    if string[var] != " ":
        return None
    return var

def count_space_end(string):
    p = len(string)
    for var in range(p):
        if string[var] == " ":
            var += 1
            break
    while var < p and string[var] == " ":
        var += 1
    return var - 1

def count_words(string):
    if len(string) == 0:
        return 0
    elif count_space_start(string) == None:
        return 1
    else:
        if count_space_start(string) == 0:
            count = 0
        else:
            count = 1
        if string == " ":
            return 0
        count += count_words(string[count_space_end(string) : len(string)])
        return count

print("The number of words in given sentence is " + str(count_words(sentence)))
