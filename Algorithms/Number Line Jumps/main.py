x1, v1, x2, v2 = map(int, input().split())
def kangaroo(x1, v1, x2, v2):
    i=1
    check=False
    while i<10000:
        if ((x1>x2) and (v1<v2)) or ((x1<x2) and (v1>v2)) and (x1+i*v1==x2+i*v2):
            print("YES")
            check=True
            break
        else:
            i+=1

    if check==False:
        print("NO")


kangaroo(x1, v1, x2, v2)

