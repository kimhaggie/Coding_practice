#11055
import sys
import math

n = int(sys.stdin.readline().rstrip('\n'))
a = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
dp = [0]*n
dp[0] = a[0]
for idx in range(1,n):
    tmp = a[idx]
    for i in range(idx):
        if a[i] < a[idx] and tmp < a[idx] + dp[i]:
            tmp = a[idx] + dp[i]
    dp[idx] = tmp
print(max(dp))