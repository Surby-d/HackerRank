x, y, z = map(int, input().split())
def reverse(n):
    rems = ""
    while n>0:
        rems+=str(n%10)
        n = n//10
    return(int(rems))

days = [i for i in range(x, y+1) if ((i-reverse(i))%z == 0)]
print(len(days))
