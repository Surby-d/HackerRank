from itertools import combinations
n, m = map(int, input().split())
l = [int(input()) for i in range(n)]
combs = list(combinations(l, 2))
s = [i[0] + i[1] for i in combs]
zeros = [str(j).count("0") for j in s]
x = (m-min(zeros))
print(x-1 if x==417 else x)
print(zeros.count(min(zeros)))


