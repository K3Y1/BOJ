import sys
from sys import flags, stdin

Input = sys.stdin.readline
n = int(Input())
m = int(Input())
numbers=[]

numbers = list(map(int, input().split()))
count = 0
if len(numbers)/2 == 1:
    for i in range((len(numbers) + 1) / 2):
        num = numbers[i]
        for j in range(i+1,len(numbers)):
            if numbers[j] == m - num:
                count+=1
else:
    for i in range(int(len(numbers) / 2)):
        num = numbers[i]
        for j in range(i+1,len(numbers)):
            if numbers[j] == m - num:
                count+=1


print(count)

