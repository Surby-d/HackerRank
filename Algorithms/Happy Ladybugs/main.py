from itertools import groupby
def happyLadybugs(s):
    # Write your code here
    b = list(s)
    state = 0
    if "_" in b:
        for i in b:
            if i!="_" and b.count(i) == 1:
                state = 1
            else:
                pass

    elif b.count("_")==len(b):
        print("YES" if len(b)>1 else "NO")

    else:
        groups = [list(j) for i, j in groupby(b)]
        for i in groups:
            if len(i) == 1:
                state = 1

    return "YES" if state == 0 else "NO"


t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    result = happyLadybugs(s)
    print(result)
