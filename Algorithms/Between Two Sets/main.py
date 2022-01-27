def factor(m, n, a, b):
    first=0
    a1=[]
    i=0
    tot=0
    for j in range(a[m-1], b[0]+1):
        first = sum([1 for k in a if j%k==0])
        if first==len(a):
            a1.append(j)


    while i<len(a1):
        b1=sum([1 for y in b if y%a1[i]==0])
        if b1==len(b):
            tot+=1

        i+=1

    print(tot)



m, n = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
factor(m, n, a, b)
