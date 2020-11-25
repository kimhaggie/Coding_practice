#11653
import sys
import math

N = int(sys.stdin.readline().rstrip('\n'))
#cutline = max(int(math.sqrt(N+1)),N+1)
cutline = 5000001
prime = [1,1] + [0 for _ in range(2,cutline)]
prime_number = []
for i in range(2,cutline):
    if prime[i] == 0:
        prime[i] = 2
        x = i + i
        prime_number.append(i)
        while x < cutline:
            prime[x] = 1
            x += i
ans = []
max_n = len(prime_number)
cur = 0
original = N
while N != 1 and prime_number[cur] <= math.sqrt(N+1)+1:
    if N % prime_number[cur]==0:
        ans.append(prime_number[cur])
        N = N/prime_number[cur]
    else:
        cur += 1

if len(ans) == 0 and N!=1:
    print(N)
else:
    print('\n'.join(map(str,ans)))