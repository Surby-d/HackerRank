t = int(input())
def findDigits(n):
    count = 0
    temp = str(n)
    for i in temp:
        if int(i)==0:
            pass
        elif n % int(i) == 0:
            count += 1

    print(count)


for i in range(t):
    findDigits(int(input()))









