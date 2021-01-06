#1932
import sys
import math

n = int(sys.stdin.readline().rstrip('\n'))
a = []
for _ in range(n):
    a.append(list(map(int,sys.stdin.readline().rstrip('\n').split(' '))))
dp = a.copy()
for i in range(len(a)):
    dp[i] = [0]*len(a[i])
dp[0][0]=a[0][0]
for i in range(1,len(a)):
    for j in range(len(a[i])):
        if j==0:
            dp[i][j] = dp[i-1][0] + a[i][j]
        elif j==len(a[i])-1:
            dp[i][j] = dp[i-1][j-1] + a[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1]+a[i][j],dp[i-1][j]+a[i][j])
print(max(dp[n-1]))