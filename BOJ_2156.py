#2156
import sys
import math

n = int(sys.stdin.readline().rstrip('\n'))
a = [0]
for _ in range(n):
    a.append(int(sys.stdin.readline().rstrip('\n')))
dp = [0]+[[0,0,0] for _ in range(n)]
dp[1] = [0,a[1],0]
for idx in range(2,n+1):
    dp[idx][0] = max([dp[idx-1][0],dp[idx-1][1],dp[idx-1][2]])
    dp[idx][1] = dp[idx-1][0] + a[idx]
    dp[idx][2] = dp[idx-1][1] + a[idx]
print(max(dp[n]))