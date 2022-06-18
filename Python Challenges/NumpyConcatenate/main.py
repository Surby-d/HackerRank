import numpy as np
n, m, p = map(int, input().split())
array = [[0, 0]]
for i in range(n+m):
    l = [list(map(int, input().split()))]
    array = np.concatenate((array, l))
    
print(array[1:])
    
    
    
    


