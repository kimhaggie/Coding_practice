#1929
import sys

m, n = map(int,sys.stdin.readline().rstrip('\n').split(' '))



prime = [[0,1],[1,1]] + [[i,0] for i in range(2,n+1)]
for i in range(2,n+1):
    if prime[i][1] == 0:
        prime[i][1] = 2
        x = i + i
        while x < n+1:
            prime[x][1] = 1
            x += i
ans = []
for i in range(n+1):
    if prime[i][1] == 2:
        if m <= i <= n:
            ans.append(str(i))
print('\n'.join(ans))