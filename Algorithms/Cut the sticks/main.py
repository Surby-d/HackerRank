def cutTheSticks(arr):
    while len(arr)>1:
        arr = [i-min(arr) for i in arr]
        arr = [x for x in arr if x!=0]
        if len(arr)!=0:
            print(len(arr))


n = int(input())
arr = list(map(int, input().split()))
print(n)
cutTheSticks(arr)
