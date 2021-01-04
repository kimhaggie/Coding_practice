#1912
import sys
import math

n = int(sys.stdin.readline().rstrip('\n'))
a = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
dp = [-float('inf') for _ in range(n)]
dp[0] = a[0]
ans = a[0]
for idx in range(1,n):
    if dp[idx-1]+a[idx] >= 0 and dp[idx-1]+a[idx]>a[idx]:
        dp[idx]=dp[idx-1]+a[idx]
    else:
        dp[idx]=a[idx]
    if ans < dp[idx]:
        ans = dp[idx]

print(ans)