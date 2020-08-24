def convert(words):
    for i in range(0,len(words)):
        words[i] = len(words[i])
    print (words)
    return words
words = []
a = int(input("number of words"))
for i in range(0,a):
    words.append(input())
convert(words)