#13398
import sys
import math

n = int(sys.stdin.readline().rstrip('\n'))
a = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
dp = [[-float('inf'),-float('inf')] for _ in range(n)]
dp[0] = [a[0],0]
for idx in range(1,n):
    dp[idx][0] = max(dp[idx-1][0]+a[idx],a[idx])
    dp[idx][1] = max(dp[idx-1][0],dp[idx-1][1]+a[idx])
ans=[]
for idx in range(n):
    if idx==0:
        ans.append(dp[idx][0])
    else:
        ans.append(max(dp[idx]))
print(max(ans))