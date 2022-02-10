p = int(input())
q = int(input())
m=0
for i in range(p, q+1):
    sqr = str(i**2)
    if len(sqr)==1 and int(sqr)==i:
        print(i, end=" ")
        m+=1
    elif len(sqr)>1:
        num1 = int(sqr[:len(sqr)//2])
        num2 = int(sqr[len(sqr)//2:])
        if num1+num2==i:
            print(i, end=" ")
            m+=1

if m==0:
    print("INVALID RANGE")
