import math
s = input()
row = math.floor(math.sqrt(len(s)))
col = math.ceil(math.sqrt(len(s)))

for i in range(col):
    print(s[i::col], end=" ")
