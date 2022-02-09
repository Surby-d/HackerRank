def loss(n, k, cloud):
    i=k%n ; power=100
    power -= cloud[i] * 2 + 1
    while i != 0:
        i = (i + k) % n
        power -= cloud[i] * 2 + 1

    return power

n, k = map(int, input().split())
cloud = list(map(int, input().split()))
result = loss(n, k, cloud)
print(result)
