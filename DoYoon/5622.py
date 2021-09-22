word = input()
length = len(word)

def charToNum(input):
    order = ord(input)
    if order>=65 and order<68:
        return 3
    elif order<71:
        return 4
    elif order<74:
        return 5
    elif order<77:
        return 6
    elif order<80: #6
        return 7
    elif order<84: #7
        return 8
    elif order<87:
        return 9
    elif order<91:
        return 10

sum = 0
for i in range(length):
    sum += charToNum(word[i])
print(sum)
