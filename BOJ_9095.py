#9095
import sys
import math

T = int(sys.stdin.readline().rstrip('\n'))
n=[]
for _ in range(T):
    n.append(int(sys.stdin.readline().rstrip('\n')))
dp = [1,1,2,4] + [0]*(max(n))
for i in range(max(n)+1):
    if dp[i]==0:
        dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
for i in n:
    print(dp[i])