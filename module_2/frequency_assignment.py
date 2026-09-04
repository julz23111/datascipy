##making gba.txt into a frequency  using count() method

with open('gba.txt', 'r') as f:
    allLines = f.readlines()
    allWords = []
    for line in allLines:
        allWords.extend(line.strip().split())
    
    print(allWords)
    print(len(allWords))
    
    wordFreq = {}
    for w in allWords:
        wordFreq[w] = allWords.count(w)
    
    print(wordFreq)