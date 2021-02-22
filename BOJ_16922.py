#16922
import sys
from collections import deque
import math
import copy
import heapq

a = [1,5,10,50]

def cal(x):
    if sum(x)!=N:
        return 0
    ans = 0
    for idx,val in enumerate(x):
        ans += a[idx]*val
    return ans

def DFS():
    stack = [[]]
    while stack:
        cur = stack.pop()
        if len(cur)==4:
            S.add(cal(cur))
            continue
        s = sum(cur)
        for i in reversed(range(N-s+1)):
            tmp = cur.copy()
            tmp.append(i)
            stack.append(tmp)

#I, V, X, L = 1, 5, 10, 50
N = int(sys.stdin.readline().rstrip('\n'))
S = set()
DFS()
print(len(S)-1)
