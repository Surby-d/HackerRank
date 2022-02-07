def prisoner(n,m,s):
    return((((s+m)-2)%n + 1))
    
if __name__=="__main__":
  t = int(input())
  for i in range(t):
    n, m, s = map(int, input().split())
    result = prisoner(n,m,s)
    print(result)
