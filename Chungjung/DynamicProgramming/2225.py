# <GOLD 5> 합분해

import math
import sys

def product(n,r):
    Cn = n+r-1
    Cr = r

    result = math.factorial(Cn)//(math.factorial(Cn-Cr) * math.factorial(Cr))

    return int(result)


n , m = map(int,sys.stdin.readline().split())

result = product(m,n) % 1000000000

print(result)
