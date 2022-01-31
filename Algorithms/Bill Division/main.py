def bonAppetit(bill, k, b):
    bill.pop(k)
    a = sum(bill)//2
    if a==b:
        print("Bon Appetit")

    else:
        print(b-a)


n, k = map(int, input().split())
bill = list(map(int, input().split()))
b = int(input())
bonAppetit(bill, k, b)
