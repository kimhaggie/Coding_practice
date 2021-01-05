#15988
import sys
import math

t = int(sys.stdin.readline().rstrip('\n'))
a=[]
for _ in range(t):
    n = int(sys.stdin.readline().rstrip('\n'))
    a.append(n)
if max(a)>3:
    dp = [0 for _ in range(max(a)+1)]
    dp[1]=1
    dp[2]=2
    dp[3]=4
    for idx in range(4,max(a)+1):
        dp[idx] = (dp[idx-1]+dp[idx-2]+dp[idx-3])%1000000009
    for i in a:
        print(dp[i])
else:
    for i in a:
        if i==1:
            print(1)
        if i==2:
            print(2)
        if i==3:
            print(4)