#10989
import sys
from collections import deque
import math
import copy
import heapq

N = int(sys.stdin.readline().rstrip('\n'))
A = [0 for _ in range(10001)]
for _ in range(N):
    x = int(sys.stdin.readline().rstrip('\n'))
    A[x]+=1
for idx,val in enumerate(A):
    if val!=0:
        for i in range(val):
            print(idx)