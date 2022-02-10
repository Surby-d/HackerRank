n = int(input())
arr = list(map(int, input().split()))
distance = []
for i in arr:
    if arr.count(i) > 1:
        ind = []
        for j in range(2):
            ind.append(arr.index(i))
            arr[arr.index(i)] = 0

        distance.append(abs(ind[0] - ind[1]))

dist = [x for x in distance if x != 0]
if len(distance) > 0:
    print(min(dist))

else:
    print(-1)
