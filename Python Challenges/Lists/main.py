n = int(input())
l = list()
def insertion(a, b):
    l.insert(a, b)

def removal(a):
    l.remove(a)

def appending(a):
    l.append(a)

def sorting():
    l.sort()

def popping(a):
    l.pop(a)

def reversal():
    l.reverse()

def display():
    print(l)

for i in range(n):
    s = list(input().split())
    if s[0]=="insert":
        insertion(int(s[1]), int(s[2]))
    elif s[0]=="remove":
        removal(int(s[1]))
    elif s[0]=="append":
        appending(int(s[1]))
    elif s[0]=="sort":
        sorting()
    elif s[0]=="pop":
        popping(-1)
    elif s[0]=="reverse":
        reversal()
    elif s[0]=="print":
        display()
