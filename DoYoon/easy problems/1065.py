n = int(input())
if n<100:
    print(n)
elif n<=1000:
    count = 99
    for i in range(100, n+1):
        if 2*(i//10%10) == i//100 + i%10:
            count += 1
    print(count)