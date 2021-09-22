mylist = [0]*20000
for i in range(1, 10):
    mylist[i*2] = 1

for i in range(10,100):
    mylist[i+i//10+i%10] = 1

for i in range(100, 1000):
    mylist[i+i//100+(i-i//100*100)//10+i%10] = 1

for i in range(1000, 10000):
    mylist[i+i//1000+(i-i//1000*1000)//100+i//10%10+i%10] = 1

for i in range(1,10000):
    if mylist[i]==0:
        print(i)