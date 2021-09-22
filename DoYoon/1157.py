word = input()
length = len(word)
mylist = [0]*123

for i in range(length):
    if ord(word[i]) >=97:
        mylist[ord(word[i])-32] += 1
    else:
        mylist[ord(word[i])] += 1

num = 0
for i in range(123):
    if mylist[i] == max(mylist):
       num += 1
       temp = i

if num ==1:
    print(chr(temp))
else:
    print('?')