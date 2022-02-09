import math
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    count=0
    x = int(math.sqrt(a))+1 if math.sqrt(a)!=int(math.sqrt(a)) else int(math.sqrt(a))
    y = int(math.sqrt(b))
    count = (y-x)+1
        

    print(count)
