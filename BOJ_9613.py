#9613
import sys
from itertools import combinations

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

n = int(sys.stdin.readline().rstrip('\n'))
for _ in range(n):
    A = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))[1:]
    ans = 0
    for a,b in list(combinations(A,2)):
        ans += gcd(a,b)
    print(ans)