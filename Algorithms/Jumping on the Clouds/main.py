n = int(input())
l = list(map(int, input().split()))
count = i = 0
while i<=(n-2):
    if (i+2)<n and l[i+2]==0:
        count+=1
        i+=2
    elif l[i+1]==0:
        count+=1
        i+=1

print(count)
