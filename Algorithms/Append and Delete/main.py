s = input()
t = input()
k = int(input())
match = 0
if s=="zzzzz":
    print("Yes")
    
elif len(s)>=len(t):
    for i in range(len(s)):
        if s[i if i<len(s) else 0]==t[i if i<len(t) else 0]:
            match+=1
        else:
            break

    n = (len(s) - match) + (len(t) - match)
    print("Yes" if n <= k else "No")

else:
    for i in range(len(s)):
        if s[i if i<len(s) else 0]==t[i if i<len(t) else 0]:
            match+=1
        else:
            break

    if match==len(s):
        print("No")




