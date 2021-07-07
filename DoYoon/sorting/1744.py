N = int(input())
mylist = []
numMinus = 0
numPlus = 0
numZero = 0
numOne = 0
for i in range(N):
    temp = int(input())
    mylist.append(temp)
    if temp<0: numMinus += 1
    if temp>1: numPlus += 1
    if temp==0: numZero += 1
    if temp==1: numOne += 1
mylist.sort()
#print(mylist)
sumPlus = 0
sumMinus = 0
sum = 0
Minus = mylist[0:numMinus]
Zero = mylist[numMinus:numMinus+numZero]
One = mylist[numMinus+numZero:numMinus+numZero+numOne]
Plus = mylist[numMinus+numZero+numOne:numMinus+numZero+numOne+numPlus]
#print(Minus, Zero, One, Plus)
if numPlus%2==0:
    for i in range(0, numPlus, 2):
        sumPlus += Plus[i]*Plus[i+1]
        #print(i)
if numPlus%2==1:
    for i in range(1, numPlus, 2):
        sumPlus += Plus[i]*Plus[i+1]
        #print(i)
    sumPlus += Plus[0]
#print(sumPlus)
sum += sumPlus
sum += numOne
if numMinus%2==0:
    for i in range(0, numMinus, 2):
        sumMinus += Minus[i]*Minus[i+1]
if numMinus%2==1:
    for i in range(0, numMinus-1, 2):
        sumMinus += Minus[i]*Minus[i+1]
    if len(Zero)==0: sumMinus += Minus[numMinus-1]

sum += sumMinus

print(sum)
