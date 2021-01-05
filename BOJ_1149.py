#1149
import sys
import math

n = int(sys.stdin.readline().rstrip('\n'))
col = [0]
for _ in range(n):
    R,G,B = map(int,sys.stdin.readline().rstrip('\n').split(' '))
    col.append([R,G,B])
dp = [0]+[[0, 0, 0] for _ in range(n)]
dp[1][0] = col[1][0]
dp[1][1] = col[1][1]
dp[1][2] = col[1][2]
for idx in range(2,n+1):
    #R
    dp[idx][0]=min(dp[idx-1][1]+col[idx][0], dp[idx-1][2]+col[idx][0])
    #G
    dp[idx][1]=min(dp[idx-1][0]+col[idx][1], dp[idx-1][2]+col[idx][1])
    #B
    dp[idx][2]=min(dp[idx-1][0]+col[idx][2], dp[idx-1][1]+col[idx][2])
print(min(dp[n]))