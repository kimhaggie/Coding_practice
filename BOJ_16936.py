#16936
import sys
from collections import deque
import math
import copy
import heapq

def exist(start):
    ans = [B[idx]]
    cnt = 1
    while cnt < N:
        tmp = cnt
        cur = ans[-1]
        up = cur*2
        down = cur//3
        flag = False
        if cur%3==0:
            flag = True
        if up in B:
            ans.append(up)
            cnt+=1
        if flag and down in B:
            ans.append(down)
            cnt+=1
        if tmp==cnt:
            return False
    return ans


N = int(sys.stdin.readline().rstrip('\n'))
B = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))

for idx in range(N):
    x = exist(idx)
    if x==False:
        continue
    else:
        print(*x)