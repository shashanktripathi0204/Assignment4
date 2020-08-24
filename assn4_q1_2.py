def filter_long_words(words,n):
    ans=[]
    for i in range(0,len(words)):
        if len(words[i])>n:
            ans.append(words[i])
    print(ans)
    return ans
words=[]
a=int(input())
for i in range(0,a):
    words.append(input(""))
n=int(input())
filter_long_words(words,n)