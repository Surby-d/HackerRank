t = int(input())
for _ in range(t):
    total=0
    n, c, m = map(int, input().split())
    wrapper = n//c
    n//=c
    total += n
    while wrapper>=1:
        wrapper = n//m
        total += wrapper
        rem = n%m
        n = wrapper
        n += rem


    print(total)
