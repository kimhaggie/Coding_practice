#1377
import sys
from collections import deque
import math
import copy
import heapq

n = int(sys.stdin.readline().rstrip('\n'))
a = []
for i in range(n):
    x = int(sys.stdin.readline().rstrip('\n'))
    a.append([x,i])
a.sort(key=lambda x:x[0])
max_val = 0
for idx,val in enumerate(a):
    x = val[1]-idx
    if x > 0:
        if max_val < x:
            max_val = x
print(max_val+1)