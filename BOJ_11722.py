#11722
import sys
import math

n = int(sys.stdin.readline().rstrip('\n'))
a = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
dp = [1]*n
for idx in range(1,n):
    tmp = 0
    for i in range(idx):
        if a[i] > a[idx] and tmp < dp[i] + 1:
            tmp = dp[i] + 1
    if dp[idx] < tmp:
       dp[idx] = tmp
print(max(dp))