#2225
import sys
import math

n,k = map(int,sys.stdin.readline().rstrip('\n').split(' '))
dp = [ [0,1]+[0 for _ in range(k-1)] for _ in range(n+1)]
dp[0] = [0]+[1 for j in range(k)]
dp[1] = [j for j in range(k+1)]
for i in range(1,n+1):
    for j in range(1,k+1):
        if dp[i][j] == 0:
            for l in range(0,i+1):
                dp[i][j]+=dp[l][j-1]
                dp[i][j]%=1000000000

print(dp[n][k])