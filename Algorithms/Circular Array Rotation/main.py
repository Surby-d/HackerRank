n, k, q = map(int, input().split())
arr = list(map(int, input().split()))

for j in range(k):
    arr.insert(0, arr[len(arr)-1])
    arr.pop(len(arr)-1)

for i in range(q):
    print(arr[int(input())])
