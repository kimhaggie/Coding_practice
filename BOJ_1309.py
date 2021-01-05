#1309
import sys
import math

n = int(sys.stdin.readline().rstrip('\n'))
dp = [0] + [[0,0,0] for _ in range(n)]
dp[1] = [1,1,1]
for idx in range(2,n+1):
    dp[idx][0] = (dp[idx-1][0] + dp[idx-1][1] + dp[idx-1][2])%9901
    dp[idx][1] = (dp[idx-1][0] + dp[idx-1][2])%9901
    dp[idx][2] = (dp[idx-1][0] + dp[idx-1][1])%9901
print(sum(dp[n])%9901)