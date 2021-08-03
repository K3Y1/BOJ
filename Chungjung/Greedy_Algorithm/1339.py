# <GOLD 4> 단어 수학

import sys
import operator

n = int(sys.stdin.readline().strip())

alphabet_list = []

for i in range(n):
    alphabet_list.append(sys.stdin.readline().strip())

alphabet = {}

for i in alphabet_list:
    alphabet_length = len(i)
    for k in range(alphabet_length-1, -1, -1):
        if(i[alphabet_length-k-1] in alphabet):
            alphabet[i[alphabet_length-k-1]
                     ] = alphabet[i[alphabet_length-k-1]] + 10**k
        else:
            alphabet[i[alphabet_length-k-1]] = 10**k


alphabet = sorted(alphabet.items(), key=operator.itemgetter(1))

print(alphabet)

num_max = 0
for i in range(0, len(alphabet)):
    print(9-i)
    num_max = num_max + alphabet[len(alphabet)-1-i][1]*(9-i)


print(num_max)
