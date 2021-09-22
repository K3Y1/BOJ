num_case = int(input())
for i in range(num_case):
    num_repeat, word = input().split()
    num_repeat = int(num_repeat)
    for j in range(len(word)):
        for k in range(num_repeat):
            print(word[j], end="")
    print("")