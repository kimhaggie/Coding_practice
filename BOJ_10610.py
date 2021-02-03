#10610
import sys
from collections import deque
import math
import copy
import heapq

N = list(sys.stdin.readline().rstrip('\n'))
if '0' in N:
    N.remove('0')
    N = sorted(N,reverse=True)
    check = list(map(int,N))
    if sum(check)%3 != 0:
        print(-1)
    else:
        N = int(''.join(N)+'0')
        print(N)
else:
    print(-1)