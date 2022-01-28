def birthday(n, l, d, m):
    start, end, ways = 0, m, 0
    group = list()
    for i in range(n):
        group.append(l[start + i: end + i])

    for j in group:
        if sum(j) == d:
            ways += 1

    print(ways)


n = int(input())
l = list(map(int, input().split()))
d, m = map(int, input().split())

birthday(n, l, d, m)


