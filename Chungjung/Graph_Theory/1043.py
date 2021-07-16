#<GOLD 4> 거짓말

#그래프 이론 / 그래프 탐색 / DFS (DFS 이용했음)

import sys
import copy

n , m = map(int,sys.stdin.readline().split())  # n: 사람의 수    m: 파티의 개수 

witness_list_precursor = list(map(int,sys.stdin.readline().split())) #witness_list[1:]이 전체 리스트
witness_list = copy.deepcopy(witness_list_precursor[1:])

party_list = []

for i in range(m):
    party = list(map(int,sys.stdin.readline().split()))
    party_list.append(party[1:])

stack = copy.deepcopy(witness_list)

while(stack):
    witness = stack.pop()

    index_list = []
    for index,i in enumerate(party_list):
        if(witness in i):
            index_list.append(i)
            for j in i:
                if(j not in witness_list):
                    witness_list.append(j)
                    stack.append(j)
    for i in index_list:
        party_list.remove(i)


print(len(party_list))


