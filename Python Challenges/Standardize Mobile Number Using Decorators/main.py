def wrapper(f):
    def fun(l):
        # complete the 
        result = []
        for num in l:
            num = list(num)
            i = 0
            while num[i]=='0':
                num.pop(i)
                i+=1
            string = "".join(num)
            if len(string)==10:
                s = "+91 {0} {1}".format(string[:5], string[5:])
            elif len(string)==12:
                s = "+{0} {1} {2}".format(string[:2], string[2:7], string[7:])
            else:
                s = "{0} {1} {2}".format(string[:3], string[3:8], string[8:]) 
            
            result.append(s)
            
        print(*sorted(result), sep='\n')
        return result 
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


