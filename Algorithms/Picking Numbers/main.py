n = int(input())
a = list(map(int, input().strip().split()))

def count(j, arr):
    return len(list(filter((lambda x: x == j), arr)))


res = -1
if len(a)==1:
    print(len(a))
else:
    for i in sorted(a):
        c = count(i, a) + count(i + 1, a)
        if c > res:
            res = c

    print(res)
