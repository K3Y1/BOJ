# <GOLD 3> 합

import sys
import operator

n = int(sys.stdin.readline().strip())

alphabet_list = []

for i in range(n):
    alphabet_list.append(sys.stdin.readline().strip())

alphabet = {'A': 0, 'B': 0, 'C': 0, 'D': 0,
            'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0}

none_zero = []

for i in alphabet_list:
    alphabet_length = len(i)

    for k in range(alphabet_length-1, -1, -1):
        alphabet[i[alphabet_length-k-1]
                 ] = alphabet[i[alphabet_length-k-1]] + 10**k
        if(k == alphabet_length-1 and i[alphabet_length-k-1] not in none_zero):
            none_zero.append(i[alphabet_length-k-1])


alphabet = sorted(alphabet.items(), key=operator.itemgetter(1))

# print(alphabet)
if(alphabet[0][0] in none_zero):
    for i in range(1, 10):
        if(alphabet[i][0] not in none_zero):
            k = alphabet[i]
            alphabet.remove(k)
            alphabet.insert(0, k)
            break

# print(alphabet)

num_max = 0
for i in range(0, 10):
    num_max = num_max + alphabet[i][1]*i


print(num_max)
