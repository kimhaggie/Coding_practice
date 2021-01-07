#17404
import sys
import math

n = int(sys.stdin.readline().rstrip('\n'))
a = []
for _ in range(n):
    a.append(list(map(int,sys.stdin.readline().rstrip('\n').split(' '))))
dp = [[[float('inf') for i in range(3)] for j in range(3)] for k in range(n)]
dp[0][0][0] = a[0][0]
dp[0][1][1] = a[0][1]
dp[0][2][2] = a[0][2]
for idx in range(1,n):
    dp[idx][0][0] = min(dp[idx-1][0][1] + a[idx][0], dp[idx-1][0][2] + a[idx][0])
    dp[idx][0][1] = min(dp[idx-1][0][0] + a[idx][1], dp[idx-1][0][2] + a[idx][1])
    dp[idx][0][2] = min(dp[idx-1][0][0] + a[idx][2], dp[idx-1][0][1] + a[idx][2])
    dp[idx][1][0] = min(dp[idx-1][1][1] + a[idx][0], dp[idx-1][1][2] + a[idx][0])
    dp[idx][1][1] = min(dp[idx-1][1][0] + a[idx][1], dp[idx-1][1][2] + a[idx][1])
    dp[idx][1][2] = min(dp[idx-1][1][0] + a[idx][2], dp[idx-1][1][1] + a[idx][2])
    dp[idx][2][0] = min(dp[idx-1][2][1] + a[idx][0], dp[idx-1][2][2] + a[idx][0])
    dp[idx][2][1] = min(dp[idx-1][2][0] + a[idx][1], dp[idx-1][2][2] + a[idx][1])
    dp[idx][2][2] = min(dp[idx-1][2][0] + a[idx][2], dp[idx-1][2][1] + a[idx][2])
#print(dp)
ans = dp[-1]
#print(ans)
ans[0][0]=float('inf')
ans[1][1]=float('inf')
ans[2][2]=float('inf')
print(min([min(ans[0]),min(ans[1]),min(ans[2])]))