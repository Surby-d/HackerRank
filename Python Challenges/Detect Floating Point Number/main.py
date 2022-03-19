# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def check_validity(s):
    if re.match(r'^[-+]?[0-9]*\.[0-9]+$', s):
        return True
    else:
        return False
            
if __name__=='__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        if check_validity(s):
            print("True")
        else:
            print("False")
