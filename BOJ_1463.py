#1463
import sys
import math

N = int(sys.stdin.readline().rstrip('\n'))
dp=[0,0,1,1] + [0]*(N-3)
for i in range(2,N+1):
    if dp[i]==0:
        if i%3==0 and i%2==0:
            dp[i]=min(dp[i//3]+1,min(dp[i//2]+1,dp[i-1]+1))
        elif i%3==0 and i%2!=0:
            dp[i]=min(dp[i//3]+1,dp[i-1]+1)
        elif i%3!=0 and i%2==0:
            dp[i]=min(dp[i//2]+1,dp[i-1]+1)
        else:
            dp[i]=dp[i-1]+1
print(dp[N])