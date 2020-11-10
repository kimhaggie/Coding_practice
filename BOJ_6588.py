#6588
import sys

n = 1000000
prime = [[0,1],[1,1]] + [[i,0] for i in range(2,n+1)]
for i in range(2,n+1):
    if prime[i][1] == 0:
        prime[i][1] = 2
        x = i + i
        while x < n+1:
            prime[x][1] = 1
            x += i
ans = []
for line in sys.stdin:
    n = int(line.rstrip('\n'))
    if n == 0:
        break
    for i in range(n):
        if prime[i][1]==2 and prime[n-i][1]==2:
            ans.append(str(n)+' = '+str(i)+' + '+str(n-i))
            break
        if i == n-1:
            ans.append("Goldbach's conjecture is wrong.")
print('\n'.join(ans))