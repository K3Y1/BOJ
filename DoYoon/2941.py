word = input()
length = len(word)
count = length

for i in range(length-1):
    if word[i] == 'c':
        if word[i+1] == '=' or word[i+1] == '-':
            count -= 1
    if i < length -2:
        if word[i] == 'd' and word[i+1] == 'z' and word[i+2] == '=':
            count -= 1
    if word[i] == 'd' and word[i+1] == '-':
        count -= 1
    if word[i] == 'l' and word[i+1] == 'j':
        count -= 1
    if word[i] == 'n' and word[i+1] == 'j':
        count -= 1
    if word[i] == 's' and word[i+1] == '=':
        count -= 1
    if word[i] == 'z' and word[i+1] == '=':
        count -= 1
print(count)