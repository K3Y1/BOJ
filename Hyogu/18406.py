import sys

read = sys.stdin.readline

def counter(num):

    times = 1
    count = 0

    while True:
        numCopy = num
        if numCopy / times < 1:
            break
        else:
            count+=1
            times *= 10

    return count

def sum(num):
    new = str(num)
    res = 0
    for i in range(len(new)):
        res += int(new[i])
    return res

number = int(read())
times = counter(number)
front = int(number / 10**(times/2))
rear = int(number % 10**(times/2))

if sum(front) == sum(rear):
    print("LUCKY")
else:
    print("READY")