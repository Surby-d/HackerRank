p,d, m, s = map(int, input().split())
count=0
while s>=p:
    s-=p
    p = max(p-d, m)
    count+=1

print(count)
