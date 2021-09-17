visited= []
dictionary = {}

def findAns(a,b,c):
    dictionary[(0, 0, 0)] = 1
    dictionary[(-1, 0, 0)] = 1
    dictionary[(-1, -1, 0)] = 1
    dictionary[(-1, 0, -1)] = 1
    dictionary[(-1, -1, -1)] = 1
    dictionary[(0,-1,0)] = 1
    dictionary[(0,0,-1)] = 1
    dictionary[(0,-1,-1)]=1
    dictionary[(-1, 1, 0)] = 1
    dictionary[(-1, 1, -1)] = 1
    dictionary[(-1,0,1)]=1
    dictionary[(-1, -1, 1)] = 1
    dictionary[(0, -1, 1)] = 1
    dictionary[(-1, 1, 1)] = 1
    dictionary[(0, 1, -1)] = 1
    dictionary[(0, 2, 1)] = 1
    dictionary[(0, 2, 0)] = 1

    tempa=0
    tempb=0
    tempc=0
    while 1:
        tempa+=1
        if tempa < tempb and tempb < tempc:
            dictionary[(tempa, tempb, tempc)] = \
                dictionary[(tempa, tempb, tempc - 1)] \
                + dictionary[(tempa, tempb - 1, tempc - 1)] \
                - dictionary[(tempa, tempb - 1, tempc)]
        else:
            dictionary[(tempa, tempb, tempc)] = \
                dictionary[(tempa - 1, tempb, tempc)] +\
                dictionary[(tempa - 1, tempb - 1, tempc)] \
                + dictionary[(tempa - 1, tempb, tempc - 1)] - \
                dictionary[(tempa - 1, tempb - 1, tempc - 1)]
        if tempa==a and tempb==b and tempc == c:
            return dictionary[(a,b,c)]
        tempa-=1
        tempb+=1
        if tempa < tempb and tempb < tempc:
            dictionary[(tempa, tempb, tempc)] = \
                dictionary[(tempa, tempb, tempc - 1)] \
                + dictionary[(tempa, tempb - 1, tempc - 1)] \
                - dictionary[(tempa, tempb - 1, tempc)]
        else:
            dictionary[(tempa, tempb, tempc)] = \
                dictionary[(tempa - 1, tempb, tempc)] +\
                dictionary[(tempa - 1, tempb - 1, tempc)] \
                + dictionary[(tempa - 1, tempb, tempc - 1)] - \
                dictionary[(tempa - 1, tempb - 1, tempc - 1)]
        if tempa==a and tempb==b and tempc == c:
            return dictionary[(a,b,c)]
        tempb-=1
        tempc+=1
        if tempa < tempb and tempb < tempc:
            dictionary[(tempa, tempb, tempc)] = \
                dictionary[(tempa, tempb, tempc - 1)] \
                + dictionary[(tempa, tempb - 1, tempc - 1)] \
                - dictionary[(tempa, tempb - 1, tempc)]
        else:
            dictionary[(tempa, tempb, tempc)] = \
                dictionary[(tempa - 1, tempb, tempc)] +\
                dictionary[(tempa - 1, tempb - 1, tempc)] \
                + dictionary[(tempa - 1, tempb, tempc - 1)] - \
                dictionary[(tempa - 1, tempb - 1, tempc - 1)]
        if tempa==a and tempb==b and tempc == c:
            return dictionary[(a,b,c)]
        tempa+=1
        if tempa < tempb and tempb < tempc:
            dictionary[(tempa, tempb, tempc)] = \
                dictionary[(tempa, tempb, tempc - 1)] \
                + dictionary[(tempa, tempb - 1, tempc - 1)] \
                - dictionary[(tempa, tempb - 1, tempc)]
        else:
            dictionary[(tempa, tempb, tempc)] = \
                dictionary[(tempa - 1, tempb, tempc)] + \
                dictionary[(tempa - 1, tempb - 1, tempc)] \
                + dictionary[(tempa - 1, tempb, tempc - 1)] - \
                dictionary[(tempa - 1, tempb - 1, tempc - 1)]
        if tempa == a and tempb == b and tempc == c:
            return dictionary[(a, b, c)]
        tempa-=1
        tempb+=1
        if tempa < tempb and tempb < tempc:
            dictionary[(tempa, tempb, tempc)] = \
                dictionary[(tempa, tempb, tempc - 1)] \
                + dictionary[(tempa, tempb - 1, tempc - 1)] \
                - dictionary[(tempa, tempb - 1, tempc)]
        else:
            dictionary[(tempa, tempb, tempc)] = \
                dictionary[(tempa - 1, tempb, tempc)] + \
                dictionary[(tempa - 1, tempb - 1, tempc)] \
                + dictionary[(tempa - 1, tempb, tempc - 1)] - \
                dictionary[(tempa - 1, tempb - 1, tempc - 1)]
        if tempa == a and tempb == b and tempc == c:
            return dictionary[(a, b, c)]
        tempc-=1
        tempa+=1
        if tempa < tempb and tempb < tempc:
            dictionary[(tempa, tempb, tempc)] = \
                dictionary[(tempa, tempb, tempc - 1)] \
                + dictionary[(tempa, tempb - 1, tempc - 1)] \
                - dictionary[(tempa, tempb - 1, tempc)]
        else:
            dictionary[(tempa, tempb, tempc)] = \
                dictionary[(tempa - 1, tempb, tempc)] + \
                dictionary[(tempa - 1, tempb - 1, tempc)] \
                + dictionary[(tempa - 1, tempb, tempc - 1)] - \
                dictionary[(tempa - 1, tempb - 1, tempc - 1)]
        if tempa == a and tempb == b and tempc == c:
            return dictionary[(a, b, c)]
        tempc+=1
        if tempa < tempb and tempb < tempc:
            dictionary[(tempa, tempb, tempc)] = \
                dictionary[(tempa, tempb, tempc - 1)] \
                + dictionary[(tempa, tempb - 1, tempc - 1)] \
                - dictionary[(tempa, tempb - 1, tempc)]
        else:
            dictionary[(tempa, tempb, tempc)] = \
                dictionary[(tempa - 1, tempb, tempc)] + \
                dictionary[(tempa - 1, tempb - 1, tempc)] \
                + dictionary[(tempa - 1, tempb, tempc - 1)] - \
                dictionary[(tempa - 1, tempb - 1, tempc - 1)]
        if tempa == a and tempb == b and tempc == c:
            return dictionary[(a, b, c)]

while 1:
    a, b, c = map(int, input().split())
    tempa =a
    tempb =b
    tempc =c
    if a==-1 and b==-1 and c==-1:
        break
    if a<=0 or b<=0 or c<=0:
        a=0
        b=0
        c=0
        print("w(", tempa, ", ", tempb, ", ", tempc, ") = ", 1, sep="")
    elif a>20 or b>20 or c>20:
        a=20
        b=20
        c=20
        print("w(", tempa, ", ", tempb, ", ", tempc, ") = ", 1048576, sep="")
    else:
        ans = findAns(a,b,c)
        print("w(", tempa, ", ", tempb, ", ", tempc, ") = ", ans, sep="")