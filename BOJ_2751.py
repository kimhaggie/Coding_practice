#2751
import sys
from collections import deque
import math
import copy
import heapq

N = int(sys.stdin.readline().rstrip('\n'))
A = []
for _ in range(N):
    A.append(int(sys.stdin.readline().rstrip('\n')))
A.sort()
for val in A:
    print(val)