#1934
import sys

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    return int(a*b/gcd(a,b))
    
n = int(sys.stdin.readline().rstrip('\n'))
ans = []
for _ in range(n):
    a, b = map(int,sys.stdin.readline().rstrip('\n').split(' '))
    ans.append(str(lcm(a,b)))
print('\n'.join(ans))