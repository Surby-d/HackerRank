if __name__ == '__main__':
    sl = []
    rl = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        sl.append(score)
        rl.append([score,name])
        
    rl.sort()
    setl = set(sl)
    setl.remove(min(setl))
    
    
    for i in rl:
        if i[0]==min(sl):
            rl.remove(i)
            
    for j in rl:
        if j[0]==min(setl):
            print(j[1])
