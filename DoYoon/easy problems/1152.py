import sys
sentence = input()

length = len(sentence)
if length==1 and sentence[0]==" ":
    print(0)
    sys.exit()
count = 1
for i in range(1, length-1):
    if sentence[i]==" ":
        count += 1
print(count)