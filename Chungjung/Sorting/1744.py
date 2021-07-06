# <GOLD 4> 수 묶기 
import sys

n = int(sys.stdin.readline())

array_minus = []
array_zero = []
array_one = []
array_plus = []

for i in range(n):
    number = int(sys.stdin.readline()) 
    if(number < 0):
        array_minus.append(number)
    elif(number == 0):
        array_zero.append(number)
    elif(number == 1):
        array_one.append(number)
    elif(number > 1):
        array_plus.append(number)

#array plus에 관한 연산 들 
new_array_plus = []

if(len(array_plus)%2!=0):
    array_plus.append(1)
array_plus = sorted(array_plus, reverse=True)

for i in range(0, len(array_plus)-1,2):
    new_array_plus.append(array_plus[i]*array_plus[i+1])


#array minus 관한 연산 
new_array_minus = []
array_minus = sorted(array_minus)
if(len(array_minus)%2!=0):
    if(len(array_zero)!=0):
        array_minus.pop()
    else:
        array_minus.append(1)

for i in range(0, len(array_minus)-1,2):
    new_array_minus.append(array_minus[i]*array_minus[i+1])

print(sum(new_array_minus)+sum(array_one)+sum(new_array_plus))
        


