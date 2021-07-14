import sys

Input = sys.stdin.readline
positive = []
negative = []
ans =[]
zero =[]
one =[]
n = int(Input())

for i in range(n):
    k = int(Input())
    if k ==1:
        ans.append(k)
    elif k > 0:
        positive.append(k)
    elif k < 0:
        negative.append(k)
    else:
        zero.append(k)

positive.sort(reverse=True)
negative.sort()


# print(positive)
# print(negative)
if len(negative) / 2 != 0:
    if len(zero) != 0:
        negative.append(0)
    else:
        negative.append(1)

len_nega = int(len(negative)/2)
point_n = 0
for i in range(len_nega):
    num = negative[point_n] * negative[point_n+1]
    ans.append(num)
    point_n = point_n + 2


if len(positive) / 2 != 0:
    positive.append(1)

point_p = 0
len_posi = int(len(positive)/2)
for i in range(len_posi):
    num = positive[point_p] * positive[point_p + 1]
    ans.append(num)
    point_p = point_p + 2


answer = 0
for i in range(len(ans)):
    answer = answer + ans[i]
# print(ans)
print(answer)