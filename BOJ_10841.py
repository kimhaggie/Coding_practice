#10841
import sys
from collections import deque
import math
import copy
import heapq

N = int(sys.stdin.readline().rstrip('\n'))
A = []
for _ in range(N):
    x = list(sys.stdin.readline().rstrip('\n').split(' '))
    x[0]=int(x[0])
    A.append(x)
A=sorted(A,key=lambda x:x[0])
for val in A:
    print(*val)