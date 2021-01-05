#9465
import sys
import math

t = int(sys.stdin.readline().rstrip('\n'))
for _ in range(t):
    n = int(sys.stdin.readline().rstrip('\n'))
    a = [[0 for i in range(n)] for j in range(2)]
    a[0] = [0]+list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
    a[1] = [0]+list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
    dp = [0]+[[0,0,0] for i in range(n)]
    dp[1] = [0,a[0][1],a[1][1]]
    for idx in range(2,n+1):
        dp[idx][0] = max([dp[idx-1][0],dp[idx-1][1],dp[idx-1][2]])
        dp[idx][1] = max(dp[idx-1][0]+a[0][idx],dp[idx-1][2]+a[0][idx])
        dp[idx][2] = max(dp[idx-1][0]+a[1][idx],dp[idx-1][1]+a[1][idx])
    print(max(dp[n]))
    #print(dp)