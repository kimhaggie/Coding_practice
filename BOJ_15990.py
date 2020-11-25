#15990
import sys
import math

T = int(sys.stdin.readline().rstrip('\n'))
n = []
for _ in range(T):
    n.append(int(sys.stdin.readline().rstrip('\n')))
dp =    [[0,1,0,1] + [0]*(max(n)-1),
        [0,0,1,1] + [0]*(max(n)-2),
        [0,0,0,1] + [0]*(max(n)-3)]

for i in range(4,max(n)+1):
    dp[0][i] = (dp[1][i-1] + dp[2][i-1])%1000000009
    dp[1][i] = (dp[0][i-2] + dp[2][i-2])%1000000009
    dp[2][i] = (dp[0][i-3] + dp[1][i-3])%1000000009
for val in n:
    print((dp[0][val]+dp[1][val]+dp[2][val])%1000000009)