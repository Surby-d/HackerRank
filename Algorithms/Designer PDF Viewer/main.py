arr = list(map(int, input().strip().split()))
str = input()
str_list = []
for i in str:
    str_list.append(arr[ord(i)-97])

print(max(str_list)*len(str))
