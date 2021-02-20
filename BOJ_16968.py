#16968
import sys
from collections import deque
import math
import copy
import heapq

ans = 0

def DFS(path,idx):
    global ans
    if idx==len(x):
        ans += 1
        return 0
    cur = x[idx]
    if cur=='d':
        if idx==0:
            for i in range(10):
                new_path=path.copy()
                new_path.append(str(i))
                DFS(new_path,idx+1)
        else:
            for i in range(10):
                if path[idx-1]==str(i):
                    continue
                new_path = path.copy()
                new_path.append(str(i))
                DFS(new_path,idx+1)
    elif cur=='c':
        if idx==0:
            for i in range(97,97+26):
                new_path = path.copy()
                new_path.append(chr(i))
                DFS(new_path,idx+1)
        else:
            for i in range(97,97+26):
                if path[idx-1]==chr(i):
                    continue
                new_path = path.copy()
                new_path.append(chr(i))
                DFS(new_path,idx+1)

x = list(sys.stdin.readline().rstrip('\n'))
DFS([],0)
print(ans)