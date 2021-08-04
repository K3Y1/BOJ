# <GOLD 1> 동전 뒤집기

import sys

n = int(sys.stdin.readline().strip())



# H는 앞 T는 뒤 / 뒷면이 제일 적게 나오도록 구해야함 

coin_map = []
for i in range(n):
    coin_line = sys.stdin.readline().strip()
    coin_line_list = []
    for k in coin_line:
        coin_line_list.append(k)
    coin_map.append(coin_line_list)

#print(coin_map)

minimum_T = 401

for loop in range(0,1<<n):
    
    Total_T = 0

    for column in range(n):
        column_T = 0

        for row in range(n):

            if(loop & (1<<row)):
                current_location = 'T' if coin_map[column][row] == 'H' else 'H'
            else:
                current_location = coin_map[column][row]
            
            if(current_location=='T'):
                column_T = column_T+1
        Total_T = Total_T + min(n-column_T , column_T)
    
    minimum_T = min(minimum_T , Total_T)

print(minimum_T)
            




