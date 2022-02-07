t = int(input())
for i in range(t):
    height = 0
    n = int(input())
    for j in range(n+1):
        if j%2 == 0:
            height+=1
        else:
            height=(2*height)


    print(height)
