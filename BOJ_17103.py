#17103
import sys
import math
n = int(sys.stdin.readline().rstrip('\n'))
A=[]
for _ in range(n):
    A.append(int(sys.stdin.readline().rstrip('\n')))
max_A = max(A)

prime = [[0,1],[1,1]] + [[i,0] for i in range(2,max_A+1)]
for i in range(2,max_A+1):
    if prime[i][1] == 0:
        prime[i][1] = 2
        x = i + i
        while x < max_A+1:
            prime[x][1] = 1
            x += i

for val in A:
    ans=0
    for i in range(int(val/2)+1):
        if prime[i][1]==2 and prime[val-i][1]==2:
            ans+=1
    print(ans)