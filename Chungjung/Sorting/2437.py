# <GOLD 3> 저울

import sys

n = int(sys.stdin.readline().strip())

balance_weight_list = list(map(int, sys.stdin.readline().split()))

balance_weight_list = sorted(balance_weight_list)

balance = 1

for i in balance_weight_list:
    if(balance<i):
        break
    balance = balance+i

print(balance)
