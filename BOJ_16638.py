#16638
import sys
from collections import deque
import math
import copy
import heapq
from itertools import combinations

def compute(path):
    result = []
    idx = 0
    while idx<N:
        # print(idx)
        if idx in path:
            sub = line[idx:idx+3]
            # print(sub)
            result.append(str(eval(sub)))
            idx += 3
        else:
            result.append(line[idx])
            idx+=1
    return ''.join(result)

ans = -float('inf')

def DFS(start, path):
    global ans
    if start>=n:
        return 0
    else:
        for idx in range(start,n):
            path.append(idx*2)
            x = eval(compute(path))
            ans = max(x,ans)
            DFS(idx+2, path)
            path.pop()


N = int(sys.stdin.readline().rstrip('\n'))
n = N//2
line = sys.stdin.readline().rstrip('\n')
if N==1:
    print(line)
else:
    DFS(0, [])
    print(ans)