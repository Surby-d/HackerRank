n = int(input())
s = []
for _ in range(n):
    s.append(list(input()))

for i in range(1, n-1):
    for j in range(1, n-1):
        if s[i][j] > max(s[i-1][j], s[i+1][j], s[i][j-1], s[i][j+1]):
            s[i][j]="X"

for _ in s:
    print("".join(_))
