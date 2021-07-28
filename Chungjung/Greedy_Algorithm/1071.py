# <PLATINUM 5> 소트

import sys
import copy

n = int(sys.stdin.readline().strip())

number = [0 for _ in range(1001)]

number_list = list(map(int, sys.stdin.readline().split()))


for i in number_list:
    number[i] = number[i]+1

sort_result = []
number_copy = copy.deepcopy(number)
cnt = 0

while(True):
    flag = 0
    for i in range(1001):
        if(cnt == 0 and number_copy[i] != 0):
            cnt = 1
            flag = 1
            sort_result.append(i)
            number_copy[i] = number_copy[i]-1
            break
        if(cnt == 1 and number_copy[i] != 0 and (i != (sort_result[-1]+1))):
            flag = 1
            sort_result.append(i)
            number_copy[i] = number_copy[i]-1
            break

    # print(sort_result)

    if(flag == 0 and len(number_list) != len(sort_result)):
        while(True):

            temp_flag = 0
            for t in range(1000, -1, -1):
                if(number_copy[t] != 0):
                    temp_flag = 1
                    flag_a = 0
                    # print(len(sort_result))
                    # print(sort_result)
                    for l in range(len(sort_result)-1, -1, -1):
                        if(t != sort_result[l]+1 and t+1 != sort_result[l+1]):
                            sort_result.insert(l+1, t)
                            number_copy[t] = number_copy[t]-1
                            flag_a = 1
                        if(flag_a == 1):
                            break
                    if(flag_a == 0):
                        sort_result.insert(0, t)
                if(temp_flag == 1):
                    break
            if(temp_flag == 1):
                break

    if(flag == 0 and len(number_list) == len(sort_result)):
        break


for i in sort_result:
    print(i, end=" ")
