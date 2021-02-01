#1931
import sys
from collections import deque
import math
import copy

N = int(sys.stdin.readline().rstrip('\n'))
I = []
for _ in range(N):
    I.append(list(map(int,sys.stdin.readline().rstrip('\n').split(' '))))
I = sorted(I)
I = deque(sorted(I,key = lambda i:i[1]))
end = 0
ans = 0
while I:
    cur = I.popleft()
    if cur[0] >= end:
        end = cur[1]
        ans += 1
print(ans)