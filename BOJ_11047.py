#11047
import sys
from collections import deque
import math
import copy

N, K = map(int,sys.stdin.readline().rstrip('\n').split(' '))
A = []
for _ in range(N):
    A.append(int(sys.stdin.readline().rstrip('\n')))
A = A[::-1]
idx = 0
ans = 0
while K!=0:
    if K < A[idx]:
        idx += 1
        continue
    k = K//A[idx]
    ans += k
    K -= k * A[idx]
    idx += 1
print(ans)