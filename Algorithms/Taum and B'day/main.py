t = int(input())

def cost(b, w, bc, wc, z):
    base = (b * bc) + (w * wc)
    if max(bc, wc, z)==z:
        print(base)

    elif bc>wc:
        print(base if (b*wc)+(b*z) > (b*bc) else (w*wc)+(b*wc)+(b*z))

    elif wc>bc:
        print(base if (w*bc)+(w*z) > (w*wc) else (b*bc)+(w*bc)+(w*z))

    else:
        print(base)

for i in range(t):
    b, w = map(int, input().split())
    bc, wc, z = map(int, input().split())
    cost(b,w, bc, wc, z)
