#11399
import sys
from collections import deque
import math
import copy

N = int(sys.stdin.readline().rstrip('\n'))
P = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
P = sorted(P,reverse=True)
prev_sum = 0
ans = 0
while P:
    cur = P.pop()
    ans+=(cur+prev_sum)
    prev_sum += cur
print(ans)