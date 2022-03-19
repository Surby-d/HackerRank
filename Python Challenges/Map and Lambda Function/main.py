cube = lambda x: x*x*x 

def fibonacci(n):
    # return a list of fibonacci numbers
    l = [0,1]
    if n==0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return l
    else:
        while len(l)<n:
            val = l[-1]+l[-2]
            l.append(val)
            
        return l
        
            
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
