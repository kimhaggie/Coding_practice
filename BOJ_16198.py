#16198
import sys
from collections import deque
import math

def DFS(W):
    n = len(W)
    if n == 3:
        return W[0]*W[2]
    sub_ans = 0
    for idx in range(1,n-1):
        new_W = W.copy()
        tmp = W[idx-1] * W[idx+1]
        del new_W[idx]
        tmp += DFS(new_W)
        if sub_ans < tmp:
            sub_ans = tmp
    return sub_ans

N = int(sys.stdin.readline().rstrip('\n'))
W = list(map(int,sys.stdin.readline().rstrip('\n').split(' ')))
print(DFS(W))