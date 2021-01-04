#1699
import sys
import math

n = int(sys.stdin.readline().rstrip('\n'))
dp = [i for i in range(n+1)]
target = []
for i in range(1,n+1):
    if i*i>n:
        break
    target.append(i*i)
for idx in range(1,n+1):
    if int(math.sqrt(idx))==math.sqrt(idx):
        dp[idx]=1
        continue
    ans = dp[idx]
    for i in target:
        if idx-i > 0 and dp[idx-i]+dp[i]<ans:
            ans = dp[idx-i]+dp[i]
    dp[idx]=ans
print(dp[n])