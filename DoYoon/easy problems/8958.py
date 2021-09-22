n = int(input())
temp = ""
sum = 0
adder = 0
for i in range(n):
    temp = input()
    length = len(temp)
    for j in range(length):
        if temp[j]=="X":
            adder = 0
        else:
            adder += 1
            sum += adder
    adder = 0
    print(sum)
    sum = 0