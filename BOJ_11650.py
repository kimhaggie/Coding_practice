#11650
import sys
from collections import deque
import math
import copy
import heapq

N = int(sys.stdin.readline().rstrip('\n'))
A = []
for _ in range(N):
    A.append(list(map(int,sys.stdin.readline().rstrip('\n').split(' '))))
A=sorted(A)
for val in A:
    print(*val)