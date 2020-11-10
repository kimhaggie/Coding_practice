#1978
import sys

n = int(sys.stdin.readline().rstrip('\n'))
A = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
max_A = max(A)
prime = [[0,1],[1,1]] + [[i,0] for i in range(2,max_A+1)]
for i in range(2,max_A+1):
    if prime[i][1] == 0:
        prime[i][1] = 2
        x = i + i
        while x < max_A+1:
            prime[x][1] = 1
            x += i
ans = 0
for i in range(max_A+1):
    if prime[i][1] == 2:
        if i in A:
            ans += 1
print(ans)