#2193
import sys
import math

N = int(sys.stdin.readline().rstrip('\n'))

zero = [0 for _ in range(N+1)]
one = [0 for _ in range(N+1)]
one[1] = 1
for i in range(2,N+1):
    zero[i]=one[i-1]+zero[i-1]
    one[i]=zero[i-1]
print(zero[N]+one[N])
