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
    return dp[n-1]

n = int(sys.stdin.readline().rstrip('\n'))
a = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
ans = []
for i in range(0,n):
    ans.append(increase(a[:i+1],i+1)+increase(list(reversed(a[i:])),n-i)-1)
if n==1:
    print(1)
else:
    print(max(ans))