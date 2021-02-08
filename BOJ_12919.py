#12919
import sys
from collections import deque
import math
import copy
import heapq

S = list(sys.stdin.readline().rstrip('\n'))
T = list(sys.stdin.readline().rstrip('\n'))
target = [T]
while target:
    new_target = []
    while target:
        cur = target.pop()
        if cur == S:
            print(1)
            sys.exit()
        if cur[-1]=='A' and len(cur)>=2:
            new_target.append(cur[:-1])
        if cur[0]=='B' and len(cur)>=2:
            new_target.append(cur[::-1][:-1])
    target = new_target
print(0)