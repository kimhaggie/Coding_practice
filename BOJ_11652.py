#11652
import sys
from collections import deque
import math
import copy
import heapq

N = int(sys.stdin.readline().rstrip('\n'))
A = dict()
for _ in range(N):
    x = int(sys.stdin.readline().rstrip('\n'))
    if x in A.keys():
        A[x]+=1
    else:
        A[x]=1
max_val = 0
max_idx = 0
for key in reversed(sorted(A.keys())):
    if max_val <= A[key]:
        max_val = A[key]
        max_idx = key
print(max_idx)