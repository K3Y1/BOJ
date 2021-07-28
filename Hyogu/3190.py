import sys
import collections
from collections import deque
read = sys.stdin.readline

n = int(read())
graph = [[0] * n for _ in range(n)]

dir = [[0,-1],[1,0],[0,1],[-1,0]]

k = int(read())
apple = []
for _ in range(k):
    x, y = map(int,read().split())
    graph[x-1][y-1] = 1

l = int(read())
move={}
for _ in range(l):
    x, c = read().split()
    move[int(x)] = c

def play(apple,move):
    graph[0][0] = True
    direction = 1
    snake = deque()
    count = 0
    new_x = 0
    new_y = 0
    rear_x = 0
    rear_y = 0
    graph[new_y][new_x] = 2
    snake.append((new_x, new_y))
    dir_num = 0
    # print(move[dir_num][1])
    while True:
        # print(graph)

        new_x = new_x + dir[direction][0]
        new_y = new_y + dir[direction][1]
        count += 1

        if 0<=new_x<n and 0<=new_y<n and graph[new_y][new_x] != 2:
            snake.append((new_x,new_y))

            ny = int(new_y)
            nx = int(new_x)
            if not graph[new_y][new_x] == 1:
                rear_x, rear_y = snake.popleft()
                graph[rear_y][rear_x] = 0
            graph[new_y][new_x] = 2

            if count in move.keys():
                if move[count] == 'D':
                    direction = (direction+1)%4
                else:
                    direction = (direction-1)%4

        else:
            return count



print(play(apple,move))














