#2133
import sys
import math

n = int(sys.stdin.readline().rstrip('\n'))
if n%2!=0:
    print(0)
elif n==2:
    print(3)
elif n==4:
    print(11)
else:
    dp = [0 for _ in range(n+1)]
    dp[1] = 2
    dp[2] = 3
    dp[3] = dp[2] * dp[1] + dp[1]
    for idx in range(4,n+1):
        if idx%2==0:
            dp[idx] = dp[idx-1] + dp[idx-2]
        else:
            dp[idx] = dp[idx-1]*dp[1] + dp[idx-2]
    print(dp[n])
    