# <GOLD 5> 배
import sys 

crane_num = int(sys.stdin.readline())
crane_list = list(map(int,sys.stdin.readline().split()))

box_num = int(sys.stdin.readline())
box_list = list(map(int,sys.stdin.readline().split()))

crane_list = sorted(crane_list, reverse=True)
box_list = sorted(box_list, reverse=True)

if(crane_list[0]<box_list[0]):
    print("-1")

else:
    box_crane_compare_list = []
    k = len(box_list)

    for crane_index, i in enumerate(crane_list):
        for index, j in enumerate(box_list):
            if(i>=j):
                box_crane_compare_list.append([i,k-index])
                break;

    box_crane_compare_list = sorted(box_crane_compare_list , key = lambda x : x[1])
#    print(box_crane_compare_list)
    cnt = len(box_list)
    count = 0
    while(box_crane_compare_list[len(box_crane_compare_list)-1][1] > 0 ):
        count = count+1;
        for index , i in enumerate(box_crane_compare_list):
            if(i[1]>0):
                for j in range(len(box_crane_compare_list)):
                    if(box_crane_compare_list[j][1]>0 and j>index):
                        box_crane_compare_list[j][1] = box_crane_compare_list[j][1]-1

                    if(box_crane_compare_list[j][1]==i[1] and j<index):
                        box_crane_compare_list[j][1] = box_crane_compare_list[j][1] -1
                i[1] = i[1] - 1
#                print(box_crane_compare_list)
    print(count)
