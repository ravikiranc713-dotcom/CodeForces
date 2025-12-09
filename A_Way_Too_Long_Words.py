n = int(input())
words = []
newwords = []
for i in range(n):
    words.append(input())
for word in words:
    if len(word)>10:
        newword=word[0]+str(len(word[1:len(word)-1]))+word[-1]
        newwords.append(newword)
    else:
        newwords.append(word)

for nw in newwords:
    print(nw)