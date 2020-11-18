#17087
import sys

def gcd(a,b):
    while(b!=0):
        tmp = a%b
        a=b
        b=tmp
    return a
    
N,S = map(int,sys.stdin.readline().rstrip('\n').split(' '))
A = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
for idx, val in enumerate(A):
    A[idx] = abs(val-S)
ans = A[0]
for val in A[1:]:
    ans = gcd(ans,val)
print(ans)