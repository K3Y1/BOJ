import sys
from sys import flags, stdin

Input = sys.stdin.readline
n = int(Input())
m = int(Input())
numbers=[]

numbers = list(map(int, input().split()))
numbers.sort()

f = 0
r = n -1

count = 0
while f < r:
    if numbers[r] + numbers[f] == m:
        count += 1
        r = r - 1
        f = f + 1
    elif numbers[r] + numbers[f] > m:
        r = r - 1
    else:
        f = f + 1

print(count)

