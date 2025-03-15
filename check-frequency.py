def WordCount(word):
    FreqDict = {}
    for char in word:
        if char in FreqDict:
            FreqDict[char] += 1
        else:
            FreqDict[char] = 1
    return FreqDict
    
    
    
val = input("Enter a number : ")
c = WordCount(val)
print(c)
        