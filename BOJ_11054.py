#11722
import sys
import math

def increase(a,n):
    dp = [1] * n
    for idx in range(0,n):
        tmp = 1
        for i in range(idx):
            if a[i] < a[idx] and tmp < dp[i] + 1:
                tmp = dp[i] + 1
        dp[idx] = tmp
    return dp

n = int(sys.stdin.readline().rstrip('\n'))
a = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
ans = []
dp1 = increase(a,n)
dp2 = increase(a[::-1],n)
for idx in range(n):
    ans.append(dp1[idx]+dp2[n-idx-1]-1)
if n==1:
    print(1)
else:
    print(max(ans))