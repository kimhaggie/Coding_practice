#10844
import sys
import math

N = int(sys.stdin.readline().rstrip('\n'))
dp = [[0,0] + [0]*(N-1)] + [[0,1] + [0]*(N-1) for _ in range(9)]
for i in range(2,N+1):
    dp[0][i] = (dp[1][i-1])%1000000000
    dp[1][i] = (dp[0][i-1] + dp[2][i-1])%1000000000
    dp[2][i] = (dp[1][i-1] + dp[3][i-1])%1000000000
    dp[3][i] = (dp[2][i-1] + dp[4][i-1])%1000000000
    dp[4][i] = (dp[3][i-1] + dp[5][i-1])%1000000000
    dp[5][i] = (dp[4][i-1] + dp[6][i-1])%1000000000
    dp[6][i] = (dp[5][i-1] + dp[7][i-1])%1000000000
    dp[7][i] = (dp[6][i-1] + dp[8][i-1])%1000000000
    dp[8][i] = (dp[7][i-1] + dp[9][i-1])%1000000000
    dp[9][i] = (dp[8][i-1])%1000000000
ans = 0
for i in range(10):
    ans+=dp[i][N]
print(ans%1000000000)