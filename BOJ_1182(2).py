#1182
import sys

N, S = map(int,sys.stdin.readline().rstrip('\n').split(' '))
a = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
n = 1<<(N)
ans = 0
for B in range(1,n):
    tmp = 0
    for i in range(N):
        if (1<<i & B) > 0:
            tmp += a[i]
    if tmp == S:
        ans += 1
print(ans)