#16943
import sys
from collections import deque
import math
import copy
import heapq
from itertools import combinations as C

def process(case):
    ans = []
    for idx in case:
        ans.append(A[idx])
    return ans

def DFS():
    ans = -1
    stack = [[]]
    while stack:
        cur = stack.pop()
        if len(cur)==N:
            x = process(cur)
            X = int(''.join(x))
            if len(str(X))!=N:
                continue
            if ans<X<=b:
                ans = X
        else:
            for i in range(N):#N
                if not i in cur:#N
                    tmp = cur.copy()
                    tmp.append(i)
                    stack.append(tmp)
    return ans
                
A, B = sys.stdin.readline().rstrip('\n').split(' ')
b = int(''.join(B))
N = len(A)
print(DFS())