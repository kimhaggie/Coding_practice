#16194
import sys
import math

N = int(sys.stdin.readline().rstrip('\n'))
p = [0]+list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
dp = [0,p[1]] + [0]*(N-1)
for idx,val in enumerate(dp):
    if idx == 0:
        continue
    if val == 0:
        pick = p[idx]
        for i in range(1,idx):
            if pick > dp[i]+p[idx-i]:
                pick = dp[i]+p[idx-i]
        dp[idx] = pick
print(dp[N])