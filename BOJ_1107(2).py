#1107
import sys
import math

def check(a,n):
    for val in n:
        if int(val) not in a:
            return False
    return True

n = int(sys.stdin.readline().rstrip('\n'))
m = int(sys.stdin.readline().rstrip('\n'))
if m>0:
    a = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
    b = []
    for i in range(10):
        if i in a:
            continue
        else:
            b.append(i)
    a = b
    if m==10:
        print(abs(n-100))
    else:
        ans = abs(n-100)
        for i in range(1000001):
            if check(a,str(i)):
                if abs(n-i) + len(str(i))< ans:
                    #print(i)
                    ans = abs(n-i) + len(str(i))
        print(ans)
else:
    print(min(len(str(n)),abs(n-100)))