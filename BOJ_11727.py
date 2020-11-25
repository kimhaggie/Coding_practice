#11727
import sys
import math

N = int(sys.stdin.readline().rstrip('\n'))
dp=[0,1,3] + [0]*(N-2)
for i in range(1,N+1):
    if dp[i]==0:
        dp[i]=2*dp[i-2]+dp[i-1]
print(dp[N]%10007)