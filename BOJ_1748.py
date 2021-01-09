#1748
import sys
import math

n = int(sys.stdin.readline().rstrip('\n'))
k = len(str(n))
ans = 0
for i in range(k-1):
    ans += 9*pow(10,i)*(i+1)
ans += (n-pow(10,k-1)+1)*k
print(ans)