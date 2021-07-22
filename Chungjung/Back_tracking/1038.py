# <GOLD 5> 감소하는 수 
import sys 

n = int(sys.stdin.readline().strip())

cnt = 0
number = 1

if(n>1022):
    print(-1)
    sys.exit(0)

if(n==0):
    print(0)
    sys.exit(0)

while(True):
    flag = True

    str_number = str(number)

    if(len(str_number)==1):
        pass

    else:
        for i in range(1,len(str_number)):
            if( str_number[i-1] > str_number[i] ):
                continue
            else:
                flag = False

                start = str_number[:i-1]
                mid = str(int(str_number[i-1])+1)
                end = '0'+str_number[i+1:]
                number = int(start+mid+end)
                break


    if(flag==True):
        cnt = cnt+1 
        if(cnt==n):
            break
        number=number+1

print(number)
