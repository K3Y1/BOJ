a = int(input())
b = int(input())
c = int(input())

mul = a*b*c
output = str(mul)
len = len(output)

result = [0]*10

for i in range(len):
    if output[i] == "0":
        result[0] += 1
    if output[i] == "1":
        result[1] += 1
    if output[i] == "2":
        result[2] += 1
    if output[i] == "3":
        result[3] += 1
    if output[i] == "4":
        result[4] += 1
    if output[i] == "5":
        result[5] += 1
    if output[i] == "6":
        result[6] += 1
    if output[i] == "7":
        result[7] += 1
    if output[i] == "8":
        result[8] += 1
    if output[i] == "9":
        result[9] += 1
for i in range(10):
    print(result[i])