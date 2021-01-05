#11057
import sys
import math

n = int(sys.stdin.readline().rstrip('\n'))
dp = [0] + [[0 for _ in range(10)] for _ in range(n)]
dp[1] = [1 for _ in range(10)]
for idx in range(2,n+1):
    for i in range(10):
        tmp = 0
        for j in range(i+1):
            tmp += (dp[idx-1][j])%10007
        tmp %= 10007
        dp[idx][i] = tmp
print(sum(dp[n])%10007)