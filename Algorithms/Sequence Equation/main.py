n = int(input())
p = list(map(int, input().split()))
a, b = min(p), max(p)
p.insert(0, 0)
for i in range(a, b+1):
    print(p.index(p.index(i)))
