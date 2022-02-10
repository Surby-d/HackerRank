n = int(input().strip())
unsorted = []
for _ in range(n):
    unsorted.append(input())

for i in sorted(unsorted, key=int):
    print(i)
