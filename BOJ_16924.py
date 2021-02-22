#16924
import sys
from collections import deque
import math
import copy
import heapq

def check(i,j):
    max_val = max([i,N-i,j,M-j])
    for val in reversed(range(1,max_val+1)):
        if i-val<0 or j-val<0 or i+val>=N or j+val>=M:
            continue
        flag = True
        for x in range(j-val,j+val+1):
            if m[i][x] == '.':
                flag = False
                break
        if not flag:
            continue
        for y in range(i-val,i+val+1):
            if m[y][j] == '.':
                flag = False
                break
        if not flag:
            continue
        return val
    return 0

N, M = map(int,sys.stdin.readline().rstrip('\n').split(' '))
m = []
for i in range(N):
    x = list(sys.stdin.readline().rstrip('\n'))
    m.append(x)
new_m = [['.' for _ in range(M)] for _ in range(N)]
ans = []
for i in range(N):
    for j in range(M):
        val = check(i,j)
        if val > 0:
            ans.append([i+1,j+1,val])
            # print(i,j,val)
            for y in range(i-val,i+val+1):
                new_m[y][j]='*'
            for x in range(j-val,j+val+1):
                new_m[i][x]='*'
flag = True
for i in range(N):
    for j in range(M):
        if m[i][j]!=new_m[i][j]:
            flag = False
            break
    if not flag:
        break
if flag:
    print(len(ans))
    for val in ans:
        print(*val)
else:
    print(-1)