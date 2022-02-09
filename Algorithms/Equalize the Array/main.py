n = int(input())
arr = list(map(int, input().split()))

num = max(arr, key=arr.count)
if arr.count(num)>1:
    new = [_ for _ in arr if _ == num]
    print(n - len(new))
else:
    print(n - 1)
