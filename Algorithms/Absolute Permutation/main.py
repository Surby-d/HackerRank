t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    #list1 = [i for i in range(1, n+1)]
    if k==0:
        print(*list(range(1, n+1)))
    elif (n/k)%2!=0:
        print(-1)
    else:
        list2 = []
        state = True
        for i in range(1, n+1):
            if state:
                list2.append(i+k)
            else:
                list2.append(i-k)

            if i%k==0:
                if state:
                    state=False
                else:
                    state=True

        print(*list2)


