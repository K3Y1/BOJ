N = int(input())
temp = N
count = 0
while 1:
    if N//10==0:
        N=10*N+N
        #print(N)
    else:
        N=(N//10+N%10)%10+(N%10)*10
        #print(N)
    count += 1
    if temp == N:
        break
print(count)