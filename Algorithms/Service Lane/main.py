n, t = map(int, input().split())
widths = list(map(int, input().split()))
for i in range(t):
    s, e = map(int, input().split())
    print(min(widths[s:e+1]))
