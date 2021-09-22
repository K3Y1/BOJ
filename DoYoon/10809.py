word = input()
length = len(word)
mylist = [-1]*(ord('z')+1)
for i in range(length-1, -1, -1):
    mylist[ord(word[i])]=i
for i in range(ord('a'),ord('z')+1):
    print(mylist[i], end=" ")